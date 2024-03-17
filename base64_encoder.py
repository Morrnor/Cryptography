def base64_encode(text):
    # Convert characters to ASCII - Concatenate into binary string
    binary = ''.join(format(ord(x), "08b") for x in text)

    # Calculate padding needed for binary string
    padding = (3 - len(binary) % 3) % 3

    # Split binary string into groups of 6 bits - Pad with zeros
    binary += '0' * padding  # Apply padding
    groups = [binary[i:i+6] for i in range(0, len(binary), 6)]

    # Convert each group of 6 bits to decimal and then to the corresponding Base64 character
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result = ''.join(base64_chars[int(group, 2)] for group in groups)
    
    # Add padding '=' characters as necessary
    if padding > 0:
        result += '=' * padding
    
    return result

def main():
    
    # Input text
    text = "python"

    # Organize text into binary
    binary = base64_encode(text)

    # Print organized binary string
    print(binary)

if __name__ == "__main__":
    main()
