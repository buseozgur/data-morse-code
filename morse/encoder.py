"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""
from morse.mapping import MORSE

WORD_SEPARATOR = "|"

def encode(text):
    """
    Encodes the given text into Morse code.
    Words are separated by a pipe (|) and letters by a space.
    """
    words = text.split() # fazla boşlukları temizler
    encoded_words= [encode_word(w) for w in words]
    return WORD_SEPARATOR.join(encoded_words)

def encode_word(word):
    """
    Encodes a single word into Morse code.
    Letters are separated by a space.
    """
    cipher= []
    for letter in word.upper():
        if "A" <= letter <= "Z":
            cipher.append(MORSE[letter])

    return " ".join(cipher)

if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_TEXT = "abc"
    ENCODED_TEXT = encode_word(EXAMPLE_TEXT)
    print(f"Encoded word '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")

    # Example usage for a sentence
    EXAMPLE_TEXT = "abc ABC"
    ENCODED_TEXT = encode(EXAMPLE_TEXT)
    print(f"Encoded '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")
