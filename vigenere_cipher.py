def vigenere_cipher(text, key, mode):
    # Generates key that matches the length of the text, make both key and text uppercase
    key = (key.upper() * (len(text) // len(key.upper()) + 1))[:len(text)]
    text = text.upper()

    # Variable to store the result in
    result = ""
    
    # Variable to store key index
    key_index = 0

    # Loop over each char in text
    for i in range(len(text)):

        # Check if char is an alphabetic char
        if text[i].isalpha():

            # Calculates shift amount for char based on char in key (-65 to get value between 0-25)
            shift = ord(key[key_index]) - 65

            # Checks if mode is "encrypt". If so it uses formula "Ci = (pi + kj) % 26" where (C: ciphertext, p: plaintext, k: key)
            if mode == "encrypt":
                result += chr(((ord(text[i]) - 65 + shift) % 26) + 65)

            # Checks if mode is "decrypt". If so it uses formula "Ci = (pi + kj) % 26" where (C: ciphertext, p: plaintext, k: key)
            elif mode == "decrypt":
                result += chr(((ord(text[i]) - 65 - shift) % 26) + 65)
            key_index += 1
        else:
            result += text[i]
                
    return result

def main():
    print(vigenere_cipher("python", "python", "encrypt"))
    print(vigenere_cipher("EWMOCA", "python", "decrypt"))

if __name__ == "__main__":
    main()
