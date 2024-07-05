import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
import random

# List to store all gossips
gossip_list = []

def handle_confession(scroll_text, progress_bar):
    """Handles confession process."""
    gossip = scroll_text.get(1.0, tk.END).strip()
    if gossip:
        gossip_list.append(gossip)
        messagebox.showinfo("Confession Received", "You have successfully confessed to the gossip box!")
        scroll_text.delete(1.0, tk.END)
        root.configure(bg=random.choice(["#FFC0CB", "#ADD8E6", "#90EE90", "#FFB6C1", "#FF69B4"]))
        progress_bar['value'] = 100
    else:
        messagebox.showwarning("Empty Confession", "Please enter some gossip before confessing.")

def clear_text(scroll_text):
    """Clears the text in the scrollable text widget."""
    scroll_text.delete(1.0, tk.END)

def show_mood():
    """Displays mood with emoji."""
    mood = mood_combobox.get()
    emojis = {"Happy": "😊", "Sad": "😢", "Excited": "😃", "Angry": "😠", "Neutral": "😐"}
    selected_emoji = emojis.get(mood, "😐")
    messagebox.showinfo("Mood Selection", f"You are feeling: {mood} {selected_emoji}")

def display_gossips():
    """Displays all stored gossips."""
    if gossip_list:
        all_gossips = "\n\n".join(gossip_list)
        messagebox.showinfo("Stored Gossips", all_gossips)
    else:
        messagebox.showinfo("No Gossips", "No gossips have been confessed yet.")

def create_gui():
    """Creates the GUI."""
    root = tk.Tk()
    root.title("Gossip Box")
    root.geometry("500x800")

    label = ttk.Label(root, text="Welcome to the Gossip Box", font=("Impact", 18))
    label.grid(column=0, row=0, padx=10, pady=10)

    button = ttk.Button(root, text="Confess", command=lambda: handle_confession(scroll_text, progress_bar))
    button.grid(column=0, row=1, padx=10, pady=10)

    global scroll_text
    scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
    scroll_text.grid(column=0, row=2, padx=10, pady=10)

    frame = tk.Frame(root)
    frame.grid(column=0, row=3, padx=10, pady=10)

    global radio_value
    radio_value = tk.StringVar()
    radio_value.set("Anonymous")

    radio1 = ttk.Radiobutton(frame, text="Anonymous", variable=radio_value, value="Anonymous")
    radio2 = ttk.Radiobutton(frame, text="Signed", variable=radio_value, value="Signed")
    radio3 = ttk.Radiobutton(frame, text="Nickname", variable=radio_value, value="Nickname")

    radio1.pack(side=tk.LEFT, padx=5)
    radio2.pack(side=tk.LEFT, padx=5)
    radio3.pack(side=tk.LEFT, padx=5)

    clear_button = ttk.Button(root, text="Clear Text", command=lambda: clear_text(scroll_text))
    clear_button.grid(column=0, row=4, padx=10, pady=10)

    mood_label = ttk.Label(root, text="Select Your Mood:", font=("Arial", 12))
    mood_label.grid(column=0, row=5, padx=10, pady=5)

    global mood_combobox
    mood_combobox = ttk.Combobox(root, values=["Happy", "Sad", "Excited", "Angry", "Neutral"], state="readonly")
    mood_combobox.grid(column=0, row=6, padx=10, pady=5)
    mood_combobox.current(0)

    mood_button = ttk.Button(root, text="Show Mood", command=show_mood)
    mood_button.grid(column=0, row=7, padx=10, pady=5)

    display_gossips_button = ttk.Button(root, text="Display Gossips", command=display_gossips)
    display_gossips_button.grid(column=0, row=8, padx=10, pady=10)

    progress_label = ttk.Label(root, text="Confession Progress:", font=("Arial", 12))
    progress_label.grid(column=0, row=9, padx=10, pady=5)

    global progress_bar
    progress_bar = ttk.Progressbar(root, length=200, mode='determinate')
    progress_bar.grid(column=0, row=10, padx=10, pady=5)

    style = ttk.Style()
    style.configure("TLabel", background="#F0F0F0", foreground="#333333", padding=5)
    style.configure("TButton", background="#ADD8E6", foreground="#333333", padding=5, font=("Arial", 10))
    style.configure("TRadiobutton", background="#F0F0F0", foreground="#333333", padding=5)

    return root

if __name__ == "__main__":
    root = create_gui()
    root.mainloop()
