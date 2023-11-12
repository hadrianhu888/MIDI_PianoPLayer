
class VirtualMusicSheet:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def remove_note(self, note):
        self.notes.remove(note)

    def clear_notes(self):
        self.notes = []

    def get_notes(self):
        return self.notes
