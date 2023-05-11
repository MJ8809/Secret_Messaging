import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def _encrypt(self):
    try:
        shift = int(self.shift_value.get())
        self.output_text.set(self.caesar_cipher.encrypt(self.input_text.get(), shift))
    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")

def _decrypt(self):
    try:
        shift = int(self.shift_value.get())
        self.output_text.set(self.caesar_cipher.decrypt(self.input_text.get(), shift))
    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CaesarCipher:
    """CaesarCipher provides methods for encryption and decryption using the Caesar cipher."""
    # ... (rest of the CaesarCipher class)


class CaesarCipherGUI:
    """CaesarCipherGUI provides a graphical user interface for encrypting and decrypting text using the Caesar cipher."""

    def __init__(self, root):

    # ... (rest of the __init__ method)

    def _create_widgets(self):
        """Creates the input fields, labels, and buttons for the Caesar cipher GUI."""
        # ... (rest of the _create_widgets method)

    def _encrypt(self):
        try:
            shift = int(self.shift_value.get())
            self.output_text.set(self.caesar_cipher.encrypt(self.input_text.get(), shift))
        except ValueError:
            messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")

    def _decrypt(self):
        try:
            shift = int(self.shift_value.get())
            self.output_text.set(self.caesar_cipher.decrypt(self.input_text.get(), shift))
        except ValueError:
            messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")


if __name__ == "__main__":
    root = tk.Tk()
    gui = CaesarCipherGUI(root)
    root.mainloop()
