import unittest
from unittest.mock import patch
from src.virtualPiano import VirtualPiano


class TestVirtualPiano(unittest.TestCase):

    def setUp(self):
        self.piano = VirtualPiano(num_octaves=2, starting_note='C')

    def test_press_key(self):
        self.piano.press_key('C', 0)
        self.assertTrue(self.piano.is_key_pressed('C', 0))

    def test_release_key(self):
        self.piano.press_key('C', 0)
        self.piano.release_key('C', 0)
        self.assertFalse(self.piano.is_key_pressed('C', 0))

    @patch('builtins.print')
    def test_display(self, mock_print):
        self.piano.press_key('C', 0)
        self.piano.press_key('C#', 0)
        self.piano.press_key('D', 0)
        self.piano.press_key('D#', 0)
        self.piano.press_key('E', 0)
        self.piano.press_key('F', 0)
        self.piano.press_key('F#', 0)
        self.piano.press_key('G', 0)
        self.piano.press_key('G#', 0)
        self.piano.press_key('A', 0)
        self.piano.press_key('A#', 0)
        self.piano.press_key('B', 0)
        self.piano.press_key('C', 1)
        self.piano.press_key('C#', 1)
        self.piano.press_key('D', 1)
        self.piano.press_key('D#', 1)
        self.piano.press_key('E', 1)
        self.piano.press_key('F', 1)