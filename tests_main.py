import unittest
from unittest.mock import MagicMock
import tkinter as tk
import main

class TestGossipBoxFunctions(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.scroll_text = tk.scrolledtext.ScrolledText(self.root)
        self.progress_bar = tk.Progressbar(self.root)
        main.gossip_list = []  # Clear gossip list before each test

    def test_on_button_click(self):
        # Simulate button click
        self.scroll_text.insert(tk.END, "Test gossip")
        main.on_button_click(self.scroll_text, self.root, self.progress_bar)
        # Assert that gossip_list has the expected content
        self.assertEqual(main.gossip_list, ["Test gossip"])
        # Assert that scroll_text is cleared
        self.assertEqual(self.scroll_text.get(1.0, tk.END), "\n")

    def test_clear_text(self):
        # Insert text into scroll_text
        self.scroll_text.insert(tk.END, "Test gossip")
        main.clear_text(self.scroll_text)
        # Assert that scroll_text is cleared
        self.assertEqual(self.scroll_text.get(1.0, tk.END), "\n")

    def test_show_mood(self):
        # Mock combobox and set its get method
        mock_combobox = MagicMock()
        mock_combobox.get.return_value = "Happy"
        result = main.show_mood(mock_combobox)
        # Assert the expected result format
        self.assertIn("Happy", result)
        self.assertIn("😊", result)

    def test_display_gossips_empty(self):
        result = main.display_gossips()
        self.assertEqual(result, "No gossips have been confessed yet.")

    def test_display_gossips_with_gossips(self):
        main.gossip_list = ["Gossip 1", "Gossip 2"]
        result = main.display_gossips()
        expected_result = "Gossip 1\n\nGossip 2"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
