#include <iostream>
#include <string>
#include <cctype>

std::string caesarCipher(const std::string& text, int shift, const std::string& mode) {
    const std::string alphabet = "abcdefghijklmnopqrstuvwxyz";
    const int alphabetSize = alphabet.size();
    const int asciiLowercaseA = 'a';

    // Ensure the shift value is within the range of the alphabet size
    shift %= alphabetSize;

    // Check if the mode is valid
    if (mode != "encode" && mode != "decode") {
        return "Invalid mode. Please specify 'encode' or 'decode'.";
    }

    std::string result;
    int direction = (mode == "encode") ? 1 : -1;
    int shiftedIndex;

    for (char c : text) {
        char lowercaseC = std::tolower(c);

        if (std::isalpha(lowercaseC)) {
            // Calculate shifted index using modular arithmetic
            shiftedIndex = (lowercaseC - asciiLowercaseA + direction * shift + alphabetSize) % alphabetSize;
            result += alphabet[shiftedIndex];
        }
        else {
            // If not a letter, keep unchanged
            result += c;
        }
    }
    return result;
}

int main() {
    std::cout << caesarCipher("Hello World!", 13, "encode") << std::endl;
    std::cout << caesarCipher("Uryyb Jbeyq!", 13, "decode") << std::endl;

    return 0;
}
