import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create and add widgets
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
root.mainloop()
