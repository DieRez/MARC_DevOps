import unittest
import tkinter as tk
from unittest.mock import MagicMock
from main import handle_confession, clear_text, show_mood, display_gossips

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        # Mock Tk and other GUI components
        self.root = MagicMock(tk.Tk)
        self.scroll_text = MagicMock(tk.Text)
        self.progress_bar = MagicMock()

    def test_clear_text(self):
        self.scroll_text.get.return_value = "Test text"
        clear_text(self.scroll_text)
        self.scroll_text.delete.assert_called_once()

    def test_display_gossips(self):
        global gossip_list
        gossip_list = ["Gossip 1", "Gossip 2"]
        display_gossips()
        # Add assertions for display_gossips() if needed

if __name__ == "__main__":
    unittest.main()
