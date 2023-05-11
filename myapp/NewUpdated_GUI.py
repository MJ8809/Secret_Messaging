from tkinter import *
from tkinter import messagebox

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

    :param ciphertext: the ciphertext to decrypt
    :param key: the key to use for decryption (an integer between 1 and 25, inclusive)
    :return: the decrypted plaintext
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
    try:
        plaintext = user_input.get()
        key = int(shift_entry.get())
        ciphertext = caesar_cipher_encrypt(plaintext, key)
        output_label.configure(text=ciphertext)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_message():
    try:
        ciphertext = user_input.get()
        key = int(shift_entry.get())
        plaintext = caesar_cipher_decrypt(ciphertext, key)
        output_label.configure(text=plaintext)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_message():
    user_input.delete(0, END)
    shift_entry.delete(0, END)
    output_label.configure(text="")

root = Tk()
root.title("Secret Messaging")
root.iconbitmap("icon.ico")

# get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the x and y coordinates to center the GUI on the screen
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (900 / 2)

# set the dimensions of the GUI and center it on the screen
root.geometry("900x900+{}+{}".format(int(x), int(y)))

# create a PhotoImage object for the background image and zoom it to twice its size
bg_image = PhotoImage(file="GhostRider.gif").zoom(2)

# set the size of the canvas widget to the size of the resized image
canvas_width = bg_image.width()
canvas_height = bg_image.height()

# create a canvas widget and place it at the back of the GUI
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, image=bg_image, anchor=NW)





root.mainloop()
