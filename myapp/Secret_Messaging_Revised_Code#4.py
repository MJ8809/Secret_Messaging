from tkinter import *
""" Michael Stock """
""" SDEV 140 21A """
""" 4-20-2023 """

""" Final Project GUI Application using tkinter and Git-hub """
#import tkinter as tk
#from tkinter import ttk
#from tkinter import PhotoImage
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
root = Tk()
root.geometry("800x400")

# create a PhotoImage object for the background image and zoom it to twice its size
bg_image = PhotoImage(file="picmix.gif").zoom(2)

# set the size of the canvas widget to the size of the resized image
canvas_width = bg_image.width()
canvas_height = bg_image.height()

# create a canvas widget and place it at the back of the GUI
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, image=bg_image, anchor=NW)

theLabel = Label(canvas, text="Sandi's Secret Message May 4", font=("Arial", 12, "bold"), fg="white", bg="#006699")
theLabel.place(x=200, y=10)
#theLabel_width = theLabel.winfo_width()
#theLabel_x = (canvas_width) - (theLabel_width)
#theLabel.place(x=theLabel_x, y=10)

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

output_label = Label(canvas, text="", font=("Arial", 12), width=40)
output_label.place(x=200, y=120)
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

decrypt_button = ttk.Button(mainframe, text="Decrypt", command=lambda: output_text.set(caesar_cipher_decrypt(input_text.get(), shift_value.get())))
decrypt_button.grid(column=2, row=10, sticky=tk.W)

root.mainloop()
"""