import unittest
import tkinter as tk
from main import handle_confession, clear_text, show_mood, display_gossips

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.scroll_text = tk.Text(self.root)
        self.progress_bar = tk.Progressbar(self.root)

    def test_handle_confession(self):
        self.scroll_text.insert(tk.END, "Test gossip")
        handle_confession(self.scroll_text, self.progress_bar)
        self.assertEqual(len(gossip_list), 1)
        self.assertEqual(self.scroll_text.get("1.0", tk.END).strip(), "")
        # Add more assertions as needed

    def test_clear_text(self):
        self.scroll_text.insert(tk.END, "Test text")
        clear_text(self.scroll_text)
        self.assertEqual(self.scroll_text.get("1.0", tk.END).strip(), "")

    def test_show_mood(self):
        mood_combobox = tk.Combobox(self.root, values=["Happy", "Sad", "Excited", "Angry", "Neutral"])
        mood_combobox.current(0)
        show_mood()

    def test_display_gossips(self):
        global gossip_list
        gossip_list = ["Gossip 1", "Gossip 2"]
        display_gossips()

if __name__ == "__main__":
    unittest.main()
