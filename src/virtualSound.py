
import pygame


# Initialize pygame mixer
pygame.mixer.init()

# Define the sound font and load it into pygame
sound_font = 'example_sound_font.sf2'
pygame.mixer.music.load(sound_font)

# Define the mapping between keyboard keys and notes
key_to_note = {
    pygame.K_z: 'C4',
    pygame.K_s: 'C#4',
    pygame.K_x: 'D4',
    pygame.K_d: 'D#4',
    pygame.K_c: 'E4',
    pygame.K_v: 'F4',
    pygame.K_g: 'F#4',
    pygame.K_b: 'G4',
    pygame.K_h: 'G#4',
    pygame.K_n: 'A4',
    pygame.K_j: 'A#4',
    pygame.K_m: 'B4',
    pygame.K_COMMA: 'C5',
}

# Define the mapping between notes and sound samples
note_to_sample = {
    'C4': 'example_sound_C4.wav',
    'C#4': 'example_sound_C#4.wav',
    'D4': 'example_sound_D4.wav',
    'D#4': 'example_sound_D#4.wav',
    'E4': 'example_sound_E4.wav',
    'F4': 'example_sound_F4.wav',
    'F#4': 'example_sound_F#4.wav',
    'G4': 'example_sound_G4.wav',
    'G#4': 'example_sound_G#4.wav',
    'A4': 'example_sound_A4.wav',
    'A#4': 'example_sound_A#4.wav',
    'B4': 'example_sound_B4.wav',
    'C5': 'example_sound_C5.wav',
}


# Define a function to play a note
def play_note(note):
    # Load the sound sample for the note
    sample = pygame.mixer.Sound(note_to_sample[note])
    # Play the sound sample
    sample.play()


# Define the main loop
def main_loop():
    # Start the pygame event loop
    while True:
        for event in pygame.event.get():
            # Check if the user pressed a key
            if event.type == pygame.KEYDOWN:
                # Check if the key is mapped to a note
                if event.key in key_to_note:
                    # Play the corresponding note
                    play_note(key_to_note[event.key])


# Start the main loop
if __name__ == '__main__':
    main_loop()
