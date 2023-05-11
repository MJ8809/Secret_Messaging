from tkinter import *
from tkinter import ttk

import tk as tk

""" Michael Stock """
""" SDEV 140 21A """
""" 4-20-2023 """

""" Final Project GUI Application using tkinter and Git-hub """
#import tkinter as tk
#from tkinter import ttk
#from tkinter import PhotoImage

def caesar_cipher(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            code = ord(char)
            shifted_code = code + shift

            if char.isupper():
                if shifted_code > ord('Z'):
                    shifted_code -= 26
                elif shifted_code < ord('A'):
                    shifted_code += 26
            elif char.islower():
                if shifted_code > ord('z'):
                    shifted_code -= 26
                elif shifted_code < ord('a'):
                    shifted_code += 26

            result += chr(shifted_code)
        else:
            result += char

    return result


def encrypt_message():
    input_text = user_input.get()
    shift_value = int(shift_entry.get())
    encrypted_text = caesar_cipher(input_text, shift_value)
    output_label.config(text=f"Encrypted Message: {encrypted_text}")


def decrypt_message():
    input_text = user_input.get()
    shift_value = -int(shift_entry.get())
    decrypted_text = caesar_cipher(input_text, shift_value)
    output_label.config(text=f"Decrypted Message: {decrypted_text}")


root = Tk()

theLabel = Label(root, text="Secret Messaging")
theLabel.pack()

user_input_label = Label(root, text="Enter your message:")
user_input_label.pack()
user_input = Entry(root)
user_input.pack()

shift_label = Label(root, text="Enter the shift value:")
shift_label.pack()
shift_entry = Entry(root)
shift_entry.pack()

encrypt_button = Button(root, text="Encrypt Message", command=encrypt_message)
encrypt_button.pack()

output_label = Label(root, text="")
output_label.pack()

root.mainloop()


"""def caesar_cipher_encrypt(plaintext, key):
    """
""" Encrypts plaintext using the Caesar Cipher algorithm with the given key.

    :param plaintext: the plaintext to encrypt
    :param key: the key to use for encryption (an integer between 1 and 25, inclusive)
    :return: the encrypted ciphertext"""
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
"""Decrypts ciphertext using the Caesar Cipher algorithm with the given key.

    parameter ciphertext: the ciphertext to decrypt
    parameter key: the key to use for decryption (an integer between 1 and 25, inclusive)
    return: the decrypted plaintext"""
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
    plaintext = user_input.get()
    key = int(shift_entry.get())
    ciphertext = caesar_cipher_encrypt(plaintext, key)
    output_label.configure(text=ciphertext)

def decrypt_message():
    ciphertext = user_input.get()
    key = int(shift_entry.get())
    plaintext = caesar_cipher_decrypt(ciphertext, key)
    output_label.configure(text=plaintext)


root = Tk()
root.geometry("900x900")

# create a PhotoImage object for the background image and zoom it to twice its size
bg_image = PhotoImage(file="GhostRider.gif").zoom(2)

# set the size of the canvas widget to the size of the resized image
canvas_width = bg_image.width()
canvas_height = bg_image.height()

# create a canvas widget and place it at the back of the GUI
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, image=bg_image, anchor=NW)

theLabel = Label(canvas, text="Secret Messaging", font=("Roman", 20, "bold"), fg="white", bg="#006699")
theLabel.place(x=200, y=10)
theLabel_width = theLabel.winfo_width()
theLabel_x = (canvas_width) - (theLabel_width)
theLabel.place(x=theLabel_x, y=10)

user_input_label = Label(canvas, text="Enter your message:", font=("Arial", 12))
user_input_label.place(x=50, y=50)
user_input = Entry(canvas, font=("Arial", 12))
user_input.place(x=200, y=50)

shift_label = Label(canvas, text="Enter the shift value:", font=("Arial", 12))
shift_label.place(x=50, y=80)
shift_entry = Entry(canvas, font=("Arial", 12))
shift_entry.place(x=200, y=80)

encrypt_button = Button(canvas, text="Encrypt Message", font=("Arial", 12, "bold"), command= caesar_cipher_encrypt)
encrypt_button.place(x=50, y=120)

decrypt_button = Button(canvas, text="Decrypt Message", font=("Arial", 12, "bold"), command= caesar_cipher_decrypt)
decrypt_button.place(x=50, y=150)

output_label = Label(canvas, text="", font=("Arial", 12), width=40)
output_label.place(x=200, y=120)
root.mainloop()
"""
root = tk.Tk()


root.geometry("800x400")

# create a PhotoImage object for the background image and zoom it to twice its size
bg_image = PhotoImage(file="picmix.gif").zoom(2)

# set the size of the canvas widget to the size of the resized image
canvas_width = bg_image.width()
canvas_height = bg_image.height()
# create a canvas widget and place it at the back of the GUI
canvas = Canvas(root, width=bg_image.width(), height=bg_image.height())
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg_image, anchor=NW)


root.title("Secret Messaging")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
shift_label = ttk.Label(mainframe, text="Shift:")
shift_label.grid(column=0, row=0, sticky=tk.W)

shift_value = tk.IntVar()
shift_entry = ttk.Entry(mainframe, width=5, textvariable=shift_value)
shift_entry.grid(column=1, row=0, sticky=tk.W)

input_label = ttk.Label(mainframe, text="Input:")
input_label.grid(column=0, row=1, sticky=tk.W)

input_text = tk.StringVar()
input_entry = ttk.Entry(mainframe, width=40, textvariable=input_text)
input_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

output_label = ttk.Label(mainframe, text="Output:")
output_label.grid(column=0, row=2, sticky=tk.W)

output_text = tk.StringVar()
output_entry = ttk.Entry(mainframe, width=40, textvariable=output_text)
output_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

encrypt_button = ttk.Button(mainframe, text="Encrypt", command=lambda: output_text.set(caesar_cipher_encrypt(input_text.get(), shift_value.get())))
encrypt_button.grid(column=1, row=10, sticky=tk.W)

decrypt_button = tk.Button(mainframe, text="Decrypt", command=lambda: output_text.set(caesar_cipher_decrypt(input_text.get(), shift_value.get())))
decrypt_button.grid(column=2, row=10, sticky=tk.W)

root.mainloop()
