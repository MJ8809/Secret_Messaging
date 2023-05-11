from tkinter import *
""" Michael Stock """
""" SDEV 140 21A """
""" 4-20-2023 """

""" Final Project GUI Application using tkinter and Git-hub """
#import tkinter as tk
#from tkinter import ttk
#from tkinter import PhotoImage
#from tkinter import messagebox


def caesar_cipher_encrypt(plaintext, key):
    """
    Encrypts plaintext using the Caesar Cipher algorithm with the given key.

    :parameter plaintext: the plaintext to encrypt
    :parameter key: the key to use for encryption (an integer between 1 and 25, inclusive)
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
    output_label["text"] = ciphertext
    return ciphertext


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


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

# create a label for the canvas widget and plac eit alongside the dialog box
theLabel = Label(canvas, text="Secret Messaging", font=("Roman", 20, "bold"), fg="white", bg="#006699")
theLabel.place(x=200, y=10)
theLabel_width = theLabel.winfo_width()
theLabel_x = (canvas_width) - (theLabel_width)
theLabel.place(x=theLabel_x, y=10)

# create user input label and place it at top of the interactive window ( line 1 )
user_input_label = Label(canvas, text="Enter your message:", font=("Arial", 12))
user_input_label.place(x=50, y=50)
user_input = Entry(canvas, font=("Arial", 12))
user_input.place(x=200, y=50)

# create a label to enter the the fixed distance value for message encryption
shift_label = Label(canvas, text="Enter the shift value:", font=("Arial", 12))
shift_label.place(x=50, y=80)
shift_entry = Entry(canvas, font=("Arial", 12))
shift_entry.place(x=200, y=80)

# create a button to encrypt the message
encrypt_button = Button(canvas, text="Encrypt Message", font=("Arial", 12, "bold"), command=lambda: caesar_cipher_encrypt(user_input.get(), int(shift_entry.get())))
encrypt_button.place(x=50, y=120)

# create a label for the ciphered plaintext and place it at the bottom of the interactive window
output_label = Label(canvas, text="", font=("Arial", 12), width=40)
output_label.place(x=200, y=120)

import tkinter as tk
from tkinter import messagebox

# Create a Tkinter window
window = tk.Tk()

# Define a function to display an error message box
def show_error_message():
    messagebox.showerror("Error", "An error occurred!")

# Create a button to trigger the error message box
button = tk.Button(window, text="Show Error", command=show_error_message)
button.pack()

# Run the Tkinter event loop
window.mainloop()

root.mainloop()
