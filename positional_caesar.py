def positional_caesar_encoder(text):
    # Defines the english alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Initialize an empty string to store the encoded text
    encoded_text = ""

    # Iterate through each character in the input text
    for i, char in enumerate(text.lower()):

        # Check if char is in the alphabet
        if char in alphabet:

            # Calculate the new index by adding the position index and applying modulo 26 to wrap around the alphabet
            index = (alphabet.index(char) + i) % 26

            # Append the encoded character to the encoded text
            encoded_text += alphabet[index]
        else:
            # If the character is not in the alphabet, append it as is
            encoded_text += char

    # Return the encoded text
    return encoded_text

def positional_caesar_decoder(text):
    # Defines the english alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Initialize an empty string to store the decoded text
    decoded_text = ""

    # Iterate through each character in the input text
    for i, char in enumerate(text.lower()):

        # Check if char is in the alphabet
        if char in alphabet:

            # Calculate new index by subtracting the position index and applying modulo 26 to wrap around the alphabet
            index = (alphabet.index(char) - i) % 26

            # Append the decoded character to the decoded text
            decoded_text += alphabet[index]
        else:
            # If the character is not in the alphabet, append it as is
            decoded_text += char

    # Return the decoded text
    return decoded_text

def main():

    print(positional_caesar_encoder("python"))  # Output: "pzvkss"
    print(positional_caesar_decoder("pzvkss"))  # Output: "python"

if __name__ == "__main__":
    main()
