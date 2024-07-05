import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from tkinter import messagebox
from main import on_button_click, clear_text, show_mood, display_gossips, gossip_list

class TestGossipBox(unittest.TestCase):

    @patch('main.scroll_text')
    @patch('main.messagebox')
    @patch('main.root')
    @patch('main.progress_bar')
    def test_on_button_click_with_gossip(self, mock_progress_bar, mock_root, mock_messagebox, mock_scroll_text):
        mock_scroll_text.get.return_value = "Some gossip\n"
        
        on_button_click()

        self.assertIn("Some gossip", gossip_list)
        mock_messagebox.showinfo.assert_called_with("Confession Received", "You have successfully confessed to the gossip box!")
        mock_scroll_text.delete.assert_called_with(1.0, tk.END)
        mock_progress_bar['value'] = 100
        self.assertEqual(mock_progress_bar['value'], 100)
        mock_root.configure.assert_called()

    @patch('main.scroll_text')
    @patch('main.messagebox')
    def test_on_button_click_without_gossip(self, mock_messagebox, mock_scroll_text):
        mock_scroll_text.get.return_value = "\n"
        
        on_button_click()
        
        mock_messagebox.showwarning.assert_called_with("Empty Confession", "Please enter some gossip before confessing.")
        self.assertNotIn("", gossip_list)

    @patch('main.scroll_text')
    def test_clear_text(self, mock_scroll_text):
        clear_text()
        
        mock_scroll_text.delete.assert_called_with(1.0, tk.END)

    @patch('main.messagebox')
    @patch('main.mood_combobox')
    def test_show_mood(self, mock_mood_combobox, mock_messagebox):
        mock_mood_combobox.get.return_value = "Happy"
        
        show_mood()
        
        mock_messagebox.showinfo.assert_called_with("Mood Selection", "You are feeling: Happy 😊")

    @patch('main.messagebox')
    def test_display_gossips_with_gossips(self, mock_messagebox):
        gossip_list.append("Test gossip")
        
        display_gossips()
        
        mock_messagebox.showinfo.assert_called_with("Stored Gossips", "Test gossip")

    @patch('main.messagebox')
    def test_display_gossips_without_gossips(self, mock_messagebox):
        gossip_list.clear()
        
        display_gossips()
        
        mock_messagebox.showinfo.assert_called_with("No Gossips", "No gossips have been confessed yet.")

if __name__ == '__main__':
    unittest.main()
