import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import filedialog

class CaesarCipher:
    """CaesarCipher provides methods for encryption and decryption using the Caesar cipher."""


    def encrypt(self, text, shift):
        encrypted_text = []

        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                char_code = ord(char) + shift_amount

                if char.islower():
                    if char_code <= ord('z'):
                        char_code > 26
                    else:
                        if char_code > ord('Z'):
                            char_code -= 26

                    encrypted_text.append(chr(char_code))
                else:
                    encrypted_text.append(char)

                return  " ".join(encrypted_text)

        def decrypt(self, text, shift):
            decrypted_text = []

            for char in text:
                if char.isalpha():
                    shift_amount = shift % 26
                    char_code = ord(char) - shift_amount

                    if char.islower():
                        if char_code < ord('a'):
                            char_code += 26
                    else:
                        if char_code < ord('A'):
                            char_code += 26

                    decrypted_text.append(chr(char_code))
                else:
                    decrypted_text.append(char)

                return ''.join(decrypted_text)

   """CaesarCipherGUI provides a graphical user interface for encrypting and decrypting text using the Caesar cipher."""


    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher GUI")

        self.caesar_cipher = CaesarCipher()

        self.mainframe = ttk.Frame(self.root, padding="10")
        self.mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self._create_widgets()

    def _create_widgets(self):
            """Creates the input fields, labels, and buttons for the Caesar cipher GUI."""
            # Shift
            shift_label = ttk.Label(self.mainframe, text="Shift:")
            shift_label.grid(column=0, row=0, sticky=tk.W)

            self.shift_value = tk.IntVar()
            shift_entry = ttk.Entry(self.mainframe, width=5, textvariable=self.shift_value)
            shift_entry.grid(column=1, row=0, sticky=tk.W)

            # Input
            input_label = ttk.Label(self.mainframe, text="Input:")
            input_label.grid(column=0, row=1, sticky=tk.W)

            self.input_text = tk.StringVar()
            input_entry = ttk.Entry(self.mainframe, width=40, textvariable=self.input_text)
            input_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

            # Output
            output_label = ttk.Label(self.mainframe, text="Output:")
            output_label.grid(column=0, row=2, sticky=tk.W)

            self.output_text = tk.StringVar()
            output_entry = ttk.Entry(self.mainframe, width=40, textvariable=self.output_text)
            output_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

            # Buttons
            encrypt_button = ttk.Button(self.mainframe, text="Encrypt", command=self._encrypt)
            encrypt_button.grid(column=0, row=3, sticky=tk.W)

            decrypt_button = ttk.Button(self.mainframe, text="Decrypt", command=self._decrypt)
            decrypt_button.grid(column=1, row=3, sticky=tk.W)

            save_button = ttk.Button(self.mainframe, text="Save to File", command=self._save_to_file)
            save_button.grid(column=1, row=4, sticky=tk.W)

            # Image
            image = PhotoImage(file="example_image.png")
            image_label = ttk.Label(self.mainframe, image=image)
            image_label.image = image  # Keep a reference to prevent garbage collection
            image_label.grid(column=2, row=0, rowspan=4, padx=10)

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

def _save_to_file(self):
        """Saves the output text to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.output_text.get())



if __name__ == "__main__":
    root = tk.Tk()
    gui = CaesarCipherGUI(root)
    root.mainloop()


