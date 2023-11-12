import time


class PianoKey:
    """Represents a key on a piano."""

    def __init__(self, note, octave):
        """Initialize a new PianoKey object."""
        self.note = note
        self.octave = octave
        self.is_pressed = False

    def press(self):
        """Press the key."""
        self.is_pressed = True

    def release(self):
        """Release the key."""
        self.is_pressed = False


class VirtualPiano:
    """Represents a virtual piano."""

    def __init__(self, num_octaves, starting_note='C'):
        """Initialize a new VirtualPiano object."""
        self.num_octaves = num_octaves
        self.starting_note = starting_note
        self.keys = []
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
                 'A', 'A#', 'B']
        for octave in range(num_octaves):
            for note in notes:
                key = PianoKey(note, octave)
                self.keys.append(key)

    def press_key(self, note, octave):
        """Press the specified key."""
        for key in self.keys:
            if key.note == note and key.octave == octave:
                key.press()

    def release_key(self, note, octave):
        """Release the specified key."""
        for key in self.keys:
            if key.note == note and key.octave == octave:
                key.release()

    def play_note(self, note, octave, duration):
        """Play the specified note for the specified duration."""
        self.press_key(note, octave)
        time.sleep(duration)
        self.release_key(note, octave)

    def display(self, key):
        """Display an ASCII art representation of the piano."""
        white_keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        black_keys = ['C#', 'D#', 'F#', 'G#', 'A#']
        for octave in range(self.num_octaves):
            for note in white_keys:
                key = PianoKey(note, octave)
                if key.is_pressed:
                    print('W', end='')
                else:
                    print(' ', end='')
            print()
            for note in black_keys:
                key = PianoKey(note, octave)
                if key.is_pressed:
                    print('B', end='')
                else:
                    print(' ', end='')
            print()

            for note in white_keys:
                key = f'{note}{octave}'
                if key == self.starting_note + str(octave):
                    print(' __ ', end='')
                else:
                    print('    ', end='')
                if note == 'C':
                    print('|', end='')
                else:
                    print(' ', end='')
                if self.is_key_pressed(note, octave):
                    print('X', end='')
                else:
                    print(' ', end='')
                if note == 'B':
                    print('|', end='')
                else:
                    print(' ', end='')
            print()
            for note in black_keys:
                key = f'{note}{octave}'
                if key == self.starting_note + str(octave):
                    print('     ', end='')
                else:
                    print('     ', end='')
                if self.is_key_pressed(note, octave):
                    print('X', end='')
                else:
                    print(' ', end='')
            print()

    def is_key_pressed(self, note, octave):
        """Check if the specified key is pressed."""
        for key in self.keys:
            if key.note == note and key.octave == octave:
                return key.is_pressed
        return False
                

def main(): 
    pass 


if __name__ == '__main__':
    main()