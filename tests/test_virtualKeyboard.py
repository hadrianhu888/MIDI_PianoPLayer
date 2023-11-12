import unittest
from unittest.mock import patch, Mock
from src.virtualKeyboard import VirtualKeyboard


class TestVirtualKeyboard(unittest.TestCase):

    def setUp(self):
        self.mock_piano = Mock()
        self.keyboard = VirtualKeyboard(self.mock_piano)

    def test_press_key(self):
        self.keyboard.press_key('C')
        self.mock_piano.play_note_on.assert_called_once_with('C')

    def test_release_key(self):
        self.keyboard.release_key('C')
        self.mock_piano.play_note_off.assert_called_once_with('C')