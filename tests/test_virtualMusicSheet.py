import unittest
from src.virtualMusicSheet import VirtualMusicSheet


class TestVirtualMusicSheet(unittest.TestCase):

    def setUp(self):
        self.sheet = VirtualMusicSheet()

    def test_add_note(self):
        self.sheet.add_note('C')
        self.assertEqual(self.sheet.get_notes(), ['C'])

    def test_remove_note(self):
        self.sheet.add_note('C')
        self.sheet.remove_note('C')
        self.assertEqual(self.sheet.get_notes(), [])

    def test_clear_notes(self):
        self.sheet.add_note('C')
        self.sheet.clear_notes()
        self.assertEqual(self.sheet.get_notes(), [])

    def test_get_notes(self):
        self.sheet.add_note('C')
        self.sheet.add_note('D')
        self.assertEqual(self.sheet.get_notes(), ['C', 'D'])