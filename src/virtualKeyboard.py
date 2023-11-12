
from src.virtualPiano import VirtualPiano


class VirtualKeyboard:
    def __init__(self, piano: VirtualPiano):
        self.piano = piano

    def press_key(self, key: str):
        self.piano.play_note_on(key)

    def release_key(self, key: str):
        self.piano.play_note_off(key)

