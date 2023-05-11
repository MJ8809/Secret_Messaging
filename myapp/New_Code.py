from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

def caesar_cipher_encrypt(plaintext, key):
    """
    Encrypts plaintext using the Caesar Cipher algorithm with the given key.

    :param plaintext: the plaintext to encrypt
    :param key: the key to use for encryption (an integer between 1 and 25, inclusive)
    :return: the encrypted ciphertext
    """
    if not plaintext.isalpha():
        raise ValueError("Plaintext must contain only letters")
    if not isinstance(key, int) or not 1 <= key <= 25:
        raise ValueError("Key must be an integer between 1 and 25, inclusive")
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha():
            ciphertext += chr((ord(c) - 65 + key) % 26 + 65)
        else:
            ciphertext += c
    return ciphertext

def caesar_cipher_decrypt(ciphertext, key):
    """
    Decrypts ciphertext using the Caesar Cipher algorithm with the given key.

    parameter ciphertext: the ciphertext to decrypt
    parameter key: the key to use for decryption (an integer between 1 and 25, inclusive)
    return: the decrypted plaintext
    """
    if not ciphertext.isalpha():
        raise ValueError("Ciphertext must contain only letters")
    if not isinstance(key, int) or not 1 <= key <= 25:
        raise ValueError("Key must be an integer between 1 and 25, inclusive")
    plaintext = ""
    for c in ciphertext.upper():
        if c.isalpha():
            plaintext += chr((ord(c) - 65 - key) % 26 + 65)
        else:
            plaintext += c
    return plaintext

def encrypt_message():
    message = user_input.get()
    shift = shift_entry.get()
    try:
        shift = int(shift)
        ciphertext = caesar_cipher_encrypt(message, shift)
        output_label.config(text=ciphertext)
    except ValueError as error:
        messagebox.showerror("Error", str(error))

def decrypt_message():
    message = user_input.get()
    shift = shift_entry.get()
    try:
        shift = int(shift)
        plaintext = caesar_cipher_decrypt(message, shift)
        output_label.config(text=plaintext)
    except ValueError as error:
        messagebox.showerror("Error", str(error))

def clear_message():
    user_input.delete(0, END)
    shift_entry.delete(0, END)
    output_label.config(text="")

def open_help_window():
    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.geometry("400x200")

    help_label = Label(help_window, text="This program encrypts and decrypts messages using the Caesar Cipher algorithm.", font=("Arial", 12))
    help_label.pack(pady=20)

root = Tk()
root.title("Caesar Cipher")

# create a PhotoImage object for the background image and zoom it to twice its size
bg_image = PhotoImage(file="background.gif").zoom(2)

# set the size of the canvas widget to the size of the resized image
canvas_width = bg_image.width()
canvas_height = bg_image.height()

# create a canvas widget and place it at the back of the GUI
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, image=bg_image, anchor=NW)

user_input_label = Label(root, text="Enter your message:", font=("Arial", 14), bg="#336699", fg="white")
user_input_label.place(x=50, y=50
user_input = Entry(root, font=("Arial", 14))
user_input.place(x=250, y=50)

shift_label = Label(root, text="Enter the shift value:", font=("Arial", 14), bg="#336699", fg="white")
shift_label.place(x=50, y=100)
shift_entry = Entry(root, font=("Arial", 14))
shift_entry.place(x=250, y=100)

encrypt_button = Button(root, text="Encrypt Message", font=("Arial", 14), command=encrypt_message)
encrypt_button.place(x=50, y=150)

decrypt_button = Button(root, text="Decrypt Message", font=("Arial", 14), command=decrypt_message)
decrypt_button.place(x=250, y=150)

clear_button = Button(root, text="Clear", font=("Arial", 14), command=clear_message)
clear_button.place(x=450, y=150)

help_button = Button(root, text="Help", font=("Arial", 14), command=open_help_window)
help_button.place(x=600, y=150)

output_label = Label(root, text="", font=("Arial", 14), width=40, wraplength=500, anchor=W)
output_label.place(x=50, y=200)

root.mainloop()
