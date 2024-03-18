def caesar_cipher_encoder(text, n):
    # Defines the english alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Initialize an empty string to store the encoded text
    encoded_text = ""

    # Iterate through each character in the input text
    for char in text.lower():

        # Check if char is in the alphabet
        if char in alphabet:

            # Calculate the new index by adding the position index and applying modulo 26 to wrap around the alphabet
            index = (alphabet.index(char) + n) % 26

            # Append the encoded character to the encoded text
            encoded_text += alphabet[index]
        else:
            # If the character is not in the alphabet, append it as is
            encoded_text += char

    # Return the encoded text
    return encoded_text

def caesar_cipher_decoder(text, n):
    # Defines the english alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Initialize an empty string to store the encoded text
    decoded_text = ""

    # Iterate through each character in the input text
    for char in text.lower():

        # Check if char is in the alphabet
        if char in alphabet:

            # Calculate the new index by adding the position index and applying modulo 26 to wrap around the alphabet
            index = (alphabet.index(char) - n) % 26

            # Append the encoded character to the encoded text
            decoded_text += alphabet[index]
        else:
            # If the character is not in the alphabet, append it as is
            decoded_text += char

    # Return the encoded text
    return decoded_text



def main():
    print(caesar_cipher_encoder("python", 13))
    print(caesar_cipher_decoder("clguba", 13))

if __name__ == "__main__":
    main()
