import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Generate or load encryption key
KEY_FILE = "secret.key"

def generate_key():
    """Generate a new encryption key if it does not exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    """Load the existing encryption key."""
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Ensure a key is available
generate_key()
cipher = Fernet(load_key())

def select_file():
    """Open file dialog to select a file."""
    file_path = filedialog.askopenfilename()
    return file_path

def encrypt_file():
    """Encrypt the selected file and save it with a .enc extension."""
    file_path = select_file()
    if not file_path:
        return

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)
    encrypted_file = file_path + ".enc"

    with open(encrypted_file, "wb") as file:
        file.write(encrypted_data)

    messagebox.showinfo("Success", f"File encrypted: {encrypted_file}")

def decrypt_file():
    """Decrypt the selected encrypted file and restore the original file."""
    file_path = select_file()
    if not file_path or not file_path.endswith(".enc"):
        messagebox.showwarning("Invalid File", "Please select a valid encrypted (.enc) file")
        return

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)
    original_file = file_path.replace(".enc", "")

    with open(original_file, "wb") as file:
        file.write(decrypted_data)

    messagebox.showinfo("Success", f"File decrypted: {original_file}")

# GUI Setup
app = ctk.CTk()
app.title("File Encryptor")
app.geometry("400x250")

ctk.CTkLabel(app, text="File Encryption Tool", font=("Arial", 18)).pack(pady=10)
ctk.CTkButton(app, text="Encrypt File", command=encrypt_file).pack(pady=10)
ctk.CTkButton(app, text="Decrypt File", command=decrypt_file).pack(pady=10)
ctk.CTkButton(app, text="Exit", command=app.quit).pack(pady=10)

app.mainloop()
