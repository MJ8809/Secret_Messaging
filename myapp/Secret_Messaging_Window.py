""" Michael Stock """
""" SDEV 140 21A """
""" 4-20-2023 """

""" Final Project GUI Application using tkinter, Git-hub """

# """ def function for creating general un-sized window """

from tkinter import *

"""root = Tk()
theLabel = Label(root, text="Secret Messaging")
theLabel.pack()
root.mainloop()"""

from tkinter import *



"""def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            # Shift the character by the specified amount
            shifted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            # Preserve the case of the original character
            if char.isupper():
                shifted_char = shifted_char.upper()
            cipher_text += shifted_char
        else:
            # Non-alphabetic characters are left unchanged
            cipher_text += char
    return cipher_text
"""
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

decrypt_button = Button(root, text="Decrypt Message", command=decrypt_message)
decrypt_button.pack()

output_label = Label(root, text="")
output_label.pack()

root.mainloop()

"""def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            # Shift the character by the specified amount
            shifted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            # Preserve the case of the original character
            if char.isupper():
                shifted_char = shifted_char.upper()
            cipher_text += shifted_char
        else:
            # Non-alphabetic characters are left unchanged
            cipher_text += char
    return cipher_text


# Get user input for the message and shift value
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message using the Caesar cipher
encrypted_message = caesar_cipher(message, shift)
print("Encrypted message:", encrypted_message)

# Decrypt the message using the same shift value
decrypted_message = caesar_cipher(encrypted_message, -shift)
print("Decrypted message:", decrypted_message)"""

# """def function for creating frameworks within window """

from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


"""root = Tk()"""
"""theLabel = Label(root, text="Secret Messaging")"""
"""theLabel.pack()"""
"""root.mainloop()"""

button1 = Button(topFrame, text="Enter Message", fg="red")
button2 = Button(topFrame, text="Send Message", fg="blue")
button3 = Button(bottomFrame, text="Incoming Message", fg="green")
button4 = Button(bottomFrame, text="Decrypt Message ", fg="orange")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
