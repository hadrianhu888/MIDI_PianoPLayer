import unittest
from unittest.mock import patch, Mock
from src.virtualSound import play_note


class TestVirtualSound(unittest.TestCase):

    @patch('src.virtualSound.pygame.mixer.Sound')
    def test_play_note(self, mock_sound):
        play_note('C4')
        mock_sound.assert_called_once_with('example_sound_C4.wav')
        mock_sound.return_value.play.assert_called_once()