""" Michael Stock """
""" SDEV 140 21A """
""" 4-20-2023 """

""" Final Project GUI Application using tkinter, Git-hub """

import tkinter as tk
from tkinter import ttk

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = ord(char) + shift
            if char.islower():
                encrypted_text += chr(shifted_char % 123 if shifted_char >= 97 else (shifted_char % 97) + 97)
            elif char.isupper():
                encrypted_text += chr(shifted_char % 91 if shifted_char >= 65 else (shifted_char % 65) + 65)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

root = tk.Tk()
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
encrypt_button.grid(column=0, row=3, sticky=tk.W)

decrypt_button = ttk.Button(mainframe, text="Decrypt", command=lambda: output_text.set(caesar_cipher_decrypt(input_text.get(), shift_value.get())))
decrypt_button.grid(column=1, row=3, sticky=tk.W)

root.mainloop()
