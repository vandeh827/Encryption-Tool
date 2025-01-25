# Encryption-Tool
This Python script provides a simple GUI application for encrypting and decrypting files using symmetric encryption.

## Features

* **Encryption:**
    * Encrypts files using the Fernet encryption algorithm from the `cryptography` library.
    * Saves encrypted files with a `.enc` extension.
* **Decryption:**
    * Decrypts files with the `.enc` extension.
    * Restores the original filename.
* **GUI:**
    * User-friendly interface with `customtkinter` for easy interaction.
    * Includes buttons for encryption, decryption, and exiting the application.

## Requirements

* Python 3.x
* `customtkinter`
* `cryptography`

**Install requirements:**

```bash
pip install customtkinter cryptography
