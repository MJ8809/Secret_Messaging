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


def open_help_window():
    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.geometry("300x100")
    Label(help_window, text="This program encrypts and decrypts messages using the Caesar Cipher algorithm.", font=("Arial", 12)).pack(pady=10)
    Button(help_window, text="OK", font=("Arial", 12), command=help_window.destroy).pack()


root = Tk()
root.title("Caesar Cipher")
root.geometry("500x400")

# create the background image and resize it to fit the window
bg_image = Image.open("ghost.jpg")
bg_image = bg_image.resize((500, 400), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

# create a canvas widget to display the background image
canvas = Canvas(root, width=500, height=400)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, image=bg_image, anchor=NW)

# create the GUI widgets
user_input_label = Label(root, text="Enter your message:", font=("Arial", 14), bg="#336699", fg="white")
user_input_label.place(x=200, y=50)

user_input = Entry(root, font=("Arial", 14))
user_input.place(x=200, y=50)

shift_label = Label(root, text="Enter the shift value:", font=("Arial", 14), bg="#336699", fg="white")
shift_label.place(x=50, y=90)

shift_entry = Entry(root, font=("Arial", 14))
shift_entry.place(x=200, y=90)

encrypt_button = Button(root, text="Encrypt", font=("Arial", 14, "bold"), command=encrypt_message)
encrypt_button.place(x=50, y=140)

decrypt_button = Button(root, text="Decrypt", font=("Arial", 14, "bold"), command=decrypt_message)
decrypt_button.place(x=180, y=140)

clear_button = Button(root, text="Clear", font=("Arial", 14, "bold"), command=clear_message)
clear_button.place(x=320, y=140)

output_label = Label(root, text="", font=("Arial", 14), width=40, wraplength=400)
output_label.place(x=50, y=200)

help_button = Button(root, text="Help", font=("Arial", 14), command=open_help_window)
help_button.place(x=50, y=350)

exit_button = Button(root, text="Exit", font=("Arial", 14), command=root.destroy)
exit_button.place(x=380, y=350)

root.mainloop()

