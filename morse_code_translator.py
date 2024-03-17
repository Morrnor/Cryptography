def morse_code_translator(text):
    # Define the alphabet (Latin : Morse code)
    alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                      '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--',
                      '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                      ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
                      '$': '...-..-', '@': '.--.-.'}
    
    # Check if the text consists of Morse code characters only
    if all(char in "-. " for char in text):  

        # Split the Morse code letters
        morse_letters = text.split(' ')

        # Translate each Morse code letter to Latin character
        return ''.join([latin_char for letter in morse_letters for latin_char, value in alphabet.items() if value == letter])
    else:  

        # If text conatains latin characters, translate to morse code
        return ' '.join([alphabet[char.upper()] for char in text if char.upper() in alphabet])

def main():
    # Test the function with an example
    print(morse_code_translator("... --- ..."))

if __name__ == "__main__":
    main()
