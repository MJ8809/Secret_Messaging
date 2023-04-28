import tkinter as tk

def encrypt_text():
    plaintext = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char

    output_text.delete("1.0", "end")
    output_text.insert("1.0", ciphertext)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x300")

# Create and position the input text box
input_text = tk.Text(window, height=6, width=40)
input_text.pack(pady=10)

# Create and position the shift entry field
shift_label = tk.Label(window, text="Shift:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

# Create and position the encrypt button
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.pack(pady=10)

# Create and position the output text box
output_text = tk.Text(window, height=6, width=40)
output_text.pack(pady=10)

# Start the GUI main loop
window.mainloop()
