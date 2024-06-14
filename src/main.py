import pygame
import time
from txt_morse_functions import validate_input, convert_to_morse_code, convert_to_beeps

# Initialize Pygame
try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Error initializing pygame: {e}")
    exit(1)

# Configuration section
while True:
    message = input("What message do you want to send? ")
    if validate_input(message):
        break
    else:
        print("Invalid input. Please enter a message containing only alphanumeric characters and allowed punctuation.")

while True:
    try:
        repeat = int(input("How many times should I send the code? "))
        if repeat > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

while repeat > 0:
    # Convert the message to Morse code
    morse_message = convert_to_morse_code(message)

    # Convert Morse code to beeps
    convert_to_beeps(morse_message)
    repeat -= 1

