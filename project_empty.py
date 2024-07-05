import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to be called when button is clicked
def on_button_click():
    # Show info message
    messagebox.showinfo("You have sucessfully confessed to the gossip box!")
    # Clear the scrollable text
    scroll_text.delete(1.0, tk.END)

# Function to clear the text in the scrollable text widget
def clear_text():
    scroll_text.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Gossip Box")

# Set window size
root.geometry("400x300")

# Create a label
label = tk.Label(root, text="Welcome to the Gossip Box", font=("Impact", 14))
label.grid(column=0, row=0, padx=10, pady=10)

# Create a button
button = tk.Button(root, text="Confess", command=on_button_click)
button.grid(column=0, row=1, padx=10, pady=10)

# Create a scrollable text widget
scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
scroll_text.grid(column=0, row=2, padx=10, pady=10)

# Create a frame for radio buttons
frame = tk.Frame(root)
frame.grid(column=0, row=3, padx=10, pady=10)

# Variable to hold the selected radio button value
radio_value = tk.StringVar()
radio_value.set("Option 1")

# Create radio buttons
radio1 = tk.Radiobutton(frame, text="Anonymous", variable=radio_value, value="Option 1")
radio2 = tk.Radiobutton(frame, text="Signed", variable=radio_value, value="Option 2")
radio3 = tk.Radiobutton(frame, text="Nickname", variable=radio_value, value="Option 3")

radio1.pack(side=tk.LEFT, padx=5)
radio2.pack(side=tk.LEFT, padx=5)
radio3.pack(side=tk.LEFT, padx=5)

# Create a clear button for the scrollable text widget
clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.grid(column=0, row=4, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
