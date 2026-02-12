
from morse.mapping import MORSE

REVERSE_MORSE = {code: letter for letter, code in MORSE.items()}

def decode(morse_text):
    """
    Decode the morse text to letter texts.
    """
    morse_words = [w.strip() for w in morse_text.strip().split("|") if w.strip()]
    words = [decode_word(mw) for mw in morse_words]

    return " ".join(words)
def decode_word(morse_word):
    """
    Decodes a single Morse-encoded word into text.
    """
    word = []
    for code in morse_word.split():
        if code:
            word.append(REVERSE_MORSE[code])
    return "".join(word)

if __name__ == "__main__":
    # Example usage for one word
    from morse.encoder import encode_word

    example = "hello"
    encoded = encode_word(example)
    decoded = decode_word(encoded)
    print("TEXT   :", example)
    print("MORSE  :", encoded)
    print("DECODE :", decoded)

    # Example usage for one sentence
    from morse.encoder import encode

    example = "hey, jude"
    encoded_text = encode(example)
    decoded_text = decode(encoded_text)
    print("TEXT   :", example)
    print("MORSE  :", encoded_text)
    print("DECODE :", decoded_text)
