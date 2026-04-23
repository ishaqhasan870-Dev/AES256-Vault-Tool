# ADVANCED ENCRYPTION TOOL
ADVANCED ENCRYPTION TOOL
COMPANY NAME : CODTECH IT SOLUTIONS 
NAME : SYED MOHAMMED ISHAQ HASAN  
INTERN ID : CTIS7048 
DOMAIN : Cyber Security and Ethical Hacking
DURATION: 4 WEEKS MENTOR: NEELA SANTOSH


# AES-256 Pro Vault 🛡️

A professional-grade file encryption and decryption utility built with Python. This tool uses **AES-256-GCM** (Galois/Counter Mode) to ensure both data confidentiality and integrity, wrapped in a clean, user-friendly graphical interface.

## 🚀 Features

- **Military-Grade Encryption:** Utilizes AES-256-GCM for top-tier security.
- **Robust Key Derivation:** Uses PBKDF2 with 100,000 iterations and a unique 16-byte salt for every file.
- **Integrity Protection:** Automatically detects if an encrypted file has been tampered with or corrupted.
- **User-Friendly GUI:** Simple "Browse, Password, Action" workflow built with Tkinter.
- **Privacy Focused:** Operates entirely locally; no data ever leaves your machine.

## 🛠️ Installation

### 1. Prerequisites
Ensure you have Python 3.8 or higher installed on your system. You can check your version by running:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/AES256-Vault-Tool.git](https://github.com/YOUR_USERNAME/AES256-Vault-Tool.git)
cd AES256-Vault-Tool
```

### 3. Install Dependencies
This project relies on the `cryptography` library for high-level cryptographic recipes.
```bash
pip install cryptography
```

## 📖 How to Use

1. **Launch the Application:**
   ```bash
   python vault.py
   ```
2. **Encrypting a File:**
   - Click **Browse** and select the file you want to secure.
   - Enter a strong **Master Password**.
   - Click **ENCRYPT**. A new `.vault` file will be created in the same directory.
3. **Decrypting a File:**
   - Click **Browse** and select your `.vault` file.
   - Enter the **Master Password** used during encryption.
   - Click **DECRYPT**. Your original file will be restored.

## 🔒 Security Architecture

| Component | Implementation |
| :--- | :--- |
| **Algorithm** | AES-256-GCM |
| **Key Derivation** | PBKDF2HMAC (SHA256) |
| **Iterations** | 100,000 |
| **Salt Size** | 128-bit (Randomly generated per file) |
| **Nonce/IV** | 96-bit (Unique per encryption) |

## ⚠️ Important Disclaimer
This tool uses professional-grade encryption without any backdoors. **If you lose your Master Password, the data within the `.vault` file cannot be recovered.**

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
```

### Next Steps for your GitHub:
1. **Add a License:** On your GitHub repo page, click "Add file" -> "Create new file," type `LICENSE`, and choose the **MIT License** template.
2. **Add a Screenshot:** If you can, take a screenshot of your app running, upload it to your repo, and add it to the README using `![App Screenshot](screenshot.png)`. This makes the project look much more professional!

Would you like me to help you write a **Python setup script** (`setup.py`) next, so users can install your tool as a proper system command?


```python?code_reference&code_event_index=3
readme_content = """# AES-256 Pro Vault 🛡️

A professional-grade file encryption and decryption utility built with Python. This tool uses **AES-256-GCM** (Galois/Counter Mode) to ensure both data confidentiality and integrity, wrapped in a clean, user-friendly graphical interface.

## 🚀 Features

- **Military-Grade Encryption:** Utilizes AES-256-GCM for top-tier security.
- **Robust Key Derivation:** Uses PBKDF2 with 100,000 iterations and a unique 16-byte salt for every file.
- **Integrity Protection:** Automatically detects if an encrypted file has been tampered with or corrupted.
- **User-Friendly GUI:** Simple "Browse, Password, Action" workflow built with Tkinter.
- **Privacy Focused:** Operates entirely locally; no data ever leaves your machine.

## 🛠️ Installation

### 1. Prerequisites
Ensure you have Python 3.8 or higher installed on your system. You can check your version by running:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/AES256-Vault-Tool.git](https://github.com/YOUR_USERNAME/AES256-Vault-Tool.git)
cd AES256-Vault-Tool
```

### 3. Install Dependencies
This project relies on the `cryptography` library for high-level cryptographic recipes.
```bash
pip install cryptography
```

## 📖 How to Use

1. **Launch the Application:**
   ```bash
   python vault.py
   ```
2. **Encrypting a File:**
   - Click **Browse** and select the file you want to secure.
   - Enter a strong **Master Password**.
   - Click **ENCRYPT**. A new `.vault` file will be created in the same directory.
3. **Decrypting a File:**
   - Click **Browse** and select your `.vault` file.
   - Enter the **Master Password** used during encryption.
   - Click **DECRYPT**. Your original file will be restored.

## 🔒 Security Architecture

| Component | Implementation |
| :--- | :--- |
| **Algorithm** | AES-256-GCM |
| **Key Derivation** | PBKDF2HMAC (SHA256) |
| **Iterations** | 100,000 |
| **Salt Size** | 128-bit (Randomly generated per file) |
| **Nonce/IV** | 96-bit (Unique per encryption) |

## ⚠️ Important Disclaimer
This tool uses professional-grade encryption without any backdoors. **If you lose your Master Password, the data within the `.vault` file cannot be recovered.**

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)


```
Your professional `README.md` file is ready. I have structured it to highlight the technical robustness of the project, which is essential for security-focused tools.

Your README.md file is ready
[file-tag: code-generated-file-0-1776982182878873493]

### README.md Content Preview

```markdown
# AES-256 Pro Vault 🛡️

A professional-grade file encryption and decryption utility built with Python. This tool uses **AES-256-GCM** (Galois/Counter Mode) to ensure both data confidentiality and integrity, wrapped in a clean, user-friendly graphical interface.

## 🚀 Features

- **Military-Grade Encryption:** Utilizes AES-256-GCM for top-tier security.
- **Robust Key Derivation:** Uses PBKDF2 with 100,000 iterations and a unique 16-byte salt for every file.
- **Integrity Protection:** Automatically detects if an encrypted file has been tampered with or corrupted.
- **User-Friendly GUI:** Simple "Browse, Password, Action" workflow built with Tkinter.
- **Privacy Focused:** Operates entirely locally; no data ever leaves your machine.

## 🛠️ Installation

### 1. Prerequisites
Ensure you have Python 3.8 or higher installed on your system. You can check your version by running:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/AES256-Vault-Tool.git](https://github.com/YOUR_USERNAME/AES256-Vault-Tool.git)
cd AES256-Vault-Tool
```

### 3. Install Dependencies
This project relies on the `cryptography` library for high-level cryptographic recipes.
```bash
pip install cryptography
```

## 📖 How to Use

1. **Launch the Application:**
   ```bash
   python vault.py
   ```
2. **Encrypting a File:**
   - Click **Browse** and select the file you want to secure.
   - Enter a strong **Master Password**.
   - Click **ENCRYPT**. A new `.vault` file will be created in the same directory.
3. **Decrypting a File:**
   - Click **Browse** and select your `.vault` file.
   - Enter the **Master Password** used during encryption.
   - Click **DECRYPT**. Your original file will be restored.

## 🔒 Security Architecture

| Component | Implementation |
| :--- | :--- |
| **Algorithm** | AES-256-GCM |
| **Key Derivation** | PBKDF2HMAC (SHA256) |
| **Iterations** | 100,000 |
| **Salt Size** | 128-bit (Randomly generated per file) |
| **Nonce/IV** | 96-bit (Unique per encryption) |

# output file
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/562c936d-a1b6-4c10-b173-5efff798198e" />


## ⚠️ Important Disclaimer
This tool uses professional-grade encryption without any backdoors. **If you lose your Master Password, the data within the `.vault` file cannot be recovered.**

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
```

### Next Steps for your GitHub:
1. **Add a License:** On your GitHub repo page, click "Add file" -> "Create new file," type `LICENSE`, and choose the **MIT License** template.
2. **Add a Screenshot:** If you can, take a screenshot of your app running, upload it to your repo, and add it to the README using `![App Screenshot](screenshot.png)`. This makes the project look much more professional!

Would you like me to help you write a **Python setup script** (`setup.py`) next, so users can install your tool as a proper system command?
