import tkinter as tk

# Create a function to handle button click event
def button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a label widget
label = tk.Label(window, text="Hello, GUI!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

# Start the main event loop
window.mainloop()
