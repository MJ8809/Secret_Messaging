""" Michael Stock """
""" SDEV 140 21A """
""" 4-20-2023 """

""" Final Project GUI Application using tkinter, Git-hub , breezypythongui  """


# """ def function for creating general un-sized window """

from tkinter import *

root = Tk()
theLabel = Label(root, text="Secret Messaging")
theLabel .pack()
root.mainloop()


def caesar_cipher(text, shift):
    """
    Encrypts a string using the Caesar cipher.

    Parameters:
        text (str): The string to encrypt.
        shift (int): The number of positions to shift the letters.

    Returns:
        str: The encrypted string.
    """
    result = ""

    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]

        # If the character is a letter, shift it by the specified amount
        if char.isalpha():
            # Get the ASCII code for the character
            code = ord(char)

            # Shift the code by the specified amount
            shifted_code = code + shift

            # If the shifted code is outside the range of A-Z or a-z, wrap it around
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

            # Convert the shifted code back to a character and add it to the result
            result += chr(shifted_code)
        else:
            # If the character is not a letter, leave it unchanged
            result += char

    return result

# """def function for creating frameworks within window """

from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text= "Enter Message", fg="red")
button2 = Button(topFrame, text= "Send Message", fg="blue")
button3 = Button(bottomFrame, text= "Incoming Message", fg="green")
button4 = Button(bottomFrame, text= "Decript Message ", fg="orange")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()