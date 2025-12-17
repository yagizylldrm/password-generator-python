# 🛡️ Secure Password Generator (Python)

A lightweight, terminal-based tool to generate cryptographically secure passwords.

## ✨ Features
- **Secure Randomness:** Uses the `secrets` module for high-entropy generation.
- **Customizable:** Choose length and toggle numbers/symbols.
- **Clipboard Integration:** Automatically copies the result for instant use.
- **Error Handling:** Robust input validation with custom exceptions.

## 🛠️ Installation (Arch Linux)
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yagizylldrm/password-generator-python.git](https://github.com/yagizylldrm/password-generator-python.git)
   cd password-generator-python

2. **Install requirements:**
   ```bash
   sudo pacman -S xclip (not needed if you have a clipboard manager)
   pip install pyperclip
   ```
3. **Run:**
   ```bash
   python generator.py
   ```
