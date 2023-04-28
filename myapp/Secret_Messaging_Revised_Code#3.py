import tkinter as tk

from myapp.Secret_Messaging_Revised_Code import shift_entry


# Function to perform Caesar Cipher encryption
def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

# Function to perform Caesar Cipher decryption
def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Function to perform Vigenère Cipher encryption
def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            keyword_shift = ord(keyword[keyword_index]) - ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + keyword_shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            ciphertext += char
    return ciphertext

# Function to perform Vigenère Cipher decryption
def vigenere_decrypt(ciphertext, keyword):
    keyword = keyword.upper()
    keyword_index = 0
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            keyword_shift = ord(keyword[keyword_index]) - ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - keyword_shift) % 26 + ascii_offset)
            plaintext += decrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            plaintext += char
    return plaintext

# Function to handle encryption/decryption based on selected options
def process_text(output_text=None, keyword_entry=None, shift_entry=None):
    plaintext = input_text.get("1.0", "end-1c")
    keyword = keyword_entry.get()
    shift = int(shift_entry.get())
    selected_option = option_var.get()

    if selected_option == "Caesar Cipher - Encrypt":
        ciphertext = caesar_encrypt(plaintext, shift)
    elif selected_option == "Caesar Cipher - Decrypt":
        ciphertext = caesar_decrypt(plaintext, shift)
    elif selected_option == "Vigenère Cipher - Encrypt":
        ciphertext = vigenere_encrypt(plaintext, keyword)
    elif selected_option == "Vigenère Cipher - Decrypt":
        ciphertext = vigenere_decrypt(plaintext, keyword)
    else:
        ciphertext = ""

    output_text.delete("1.0", "end")
    output_text.insert("1.0", ciphertext)

# Create the main window
window = tk.Tk()
window.title("Cipher GUI")
window.geometry("400x400")

# Create and position the input text box
input_text = tk.Text(window, height=6, width=40)
input_text.pack(pady=10)

# Create and position the option selection
options = [
    "Caesar Cipher - Encrypt",
    "Caesar Cipher - Decrypt",
    "Vigenère Cipher - Encrypt",
    "Vigenère Cipher - Decrypt"
]
option_var = tk.StringVar(window)
option_var.set(options[0])
option_menu = tk.OptionMenu(window, option_var, *options)
option_menu.pack()

# Create and position the shift entry
