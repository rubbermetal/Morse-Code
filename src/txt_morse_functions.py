import pygame
import time
import re
import os

def validate_input(input_string):
    # Allow only alphanumeric characters and some punctuation
    pattern = r"^[a-zA-Z0-9 .,?!'\"/@:;=+&()-]*$"
    if re.match(pattern, input_string):
        return True
    else:
        return False

def convert_to_morse_code(message):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
        '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    morse_message = []
    for char in message:
        if char.upper() in morse_code:
            morse_message.append(morse_code[char.upper()])
        else:
            print(f"Warning: Character '{char}' is not supported in Morse code. Skipping.")
    return ' '.join(morse_message)
def dot():
    try:
        sound_file = os.path.join(os.path.dirname(__file__), 'media/dot.wav')
        pygame.mixer.Sound(sound_file).play()
    except pygame.error as e:
        print(f"Error playing dot sound: {e}")

def dash():
    try:
        sound_file = os.path.join(os.path.dirname(__file__), 'media/dash.wav')
        pygame.mixer.Sound(sound_file).play()
    except pygame.error as e:
        print(f"Error playing dash sound: {e}")

def convert_to_beeps(morse_message):
    for code in morse_message.split(' '):
        for c in code:
            if c == '.':
                dot()
            elif c == '-':
                dash()
            time.sleep(0.1)
        time.sleep(0.3)

