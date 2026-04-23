import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

class CryptoVault:
    def __init__(self, root):
        self.root = root
        self.root.title("AES-256 Pro Vault")
        self.root.geometry("500x350")
        self.root.configure(bg="#2c3e50")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(self.root, text="Secure File Encryptor", font=("Helvetica", 18, "bold"), fg="#ecf0f1", bg="#2c3e50")
        title_label.pack(pady=20)

        # File Selection
        self.file_path = tk.StringVar()
        file_frame = tk.Frame(self.root, bg="#2c3e50")
        file_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Entry(file_frame, textvariable=self.file_path, width=40).pack(side='left', padx=5)
        tk.Button(file_frame, text="Browse", command=self.browse_file).pack(side='left')

        # Password Entry
        tk.Label(self.root, text="Enter Master Password:", fg="#ecf0f1", bg="#2c3e50").pack()
        self.password_entry = tk.Entry(self.root, show="*", width=30, font=("Helvetica", 12))
        self.password_entry.pack(pady=10)

        # Action Buttons
        btn_frame = tk.Frame(self.root, bg="#2c3e50")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="ENCRYPT", bg="#27ae60", fg="white", width=15, height=2, command=self.encrypt_action).pack(side='left', padx=10)
        tk.Button(btn_frame, text="DECRYPT", bg="#e74c3c", fg="white", width=15, height=2, command=self.decrypt_action).pack(side='left', padx=10)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.file_path.set(filename)

    def derive_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    def encrypt_action(self):
        path = self.file_path.get()
        password = self.password_entry.get()

        if not path or not password:
            messagebox.showerror("Error", "Please select a file and enter a password.")
            return

        try:
            salt = os.urandom(16)
            nonce = os.urandom(12)
            key = self.derive_key(password, salt)
            aesgcm = AESGCM(key)

            with open(path, 'rb') as f:
                data = f.read()

            ciphertext = aesgcm.encrypt(nonce, data, None)

            with open(path + ".vault", 'wb') as f:
                f.write(salt + nonce + ciphertext)

            messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {os.path.basename(path)}.vault")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_action(self):
        path = self.file_path.get()
        password = self.password_entry.get()

        if not path or not password:
            messagebox.showerror("Error", "Please select a file and enter a password.")
            return

        try:
            with open(path, 'rb') as f:
                file_data = f.read()

            salt = file_data[:16]
            nonce = file_data[16:28]
            ciphertext = file_data[28:]

            key = self.derive_key(password, salt)
            aesgcm = AESGCM(key)
            
            decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)

            output_path = path.replace(".vault", "")
            if output_path == path: # If user didn't use .vault extension
                output_path = "decrypted_" + os.path.basename(path)

            with open(output_path, 'wb') as f:
                f.write(decrypted_data)

            messagebox.showinfo("Success", "File decrypted successfully!")
        except Exception:
            messagebox.showerror("Error", "Decryption failed! Likely a wrong password or corrupted file.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoVault(root)
    root.mainloop()