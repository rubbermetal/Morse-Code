
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from txt_morse_functions import validate_input, convert_to_morse_code

def test_validate_input():
    assert validate_input("Hello World!") == True
    assert validate_input("1234567890") == True
    assert validate_input(".,?!'\"/@:;=+&()-") == True
    assert validate_input("Invalid#Character") == False
    assert validate_input("Another*Invalid^Char") == False

def test_convert_to_morse_code():
    assert convert_to_morse_code("SOS") == "... --- ..."
    assert convert_to_morse_code("HELLO") == ".... . .-.. .-.. ---"
    assert convert_to_morse_code("1 2 3") == ".---- / ..--- / ...--"
    assert convert_to_morse_code("A B C") == ".- / -... / -.-."
    assert convert_to_morse_code("Hello, World!") == ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
    assert convert_to_morse_code("Invalid#Char") == ".. -. ...- .- .-.. .. -.. -.-. .... .- .-."

def test_convert_to_morse_code_with_empty_string():
    assert convert_to_morse_code("") == ""

def test_convert_to_morse_code_with_numbers():
    assert convert_to_morse_code("123") == ".---- ..--- ...--"
    assert convert_to_morse_code("456 7890") == "....- ..... -.... / --... ---.. ----. -----"

def test_convert_to_morse_code_with_mixed_case():
    assert convert_to_morse_code("HeLLo WoRLD") == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

