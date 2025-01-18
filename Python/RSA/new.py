from sympy import mod_inverse

class RSA:
    def __init__(self):
        pass

    @staticmethod
    def decrypt_prime_n(ciphertext, e, n):
        # When n is prime, phi(n) = n - 1
        phi_n = n - 1
        # Compute the private key d
        d = mod_inverse(e, phi_n)
        # Decrypt the ciphertext
        plaintext_number = pow(ciphertext, d, n)
        # Convert the plaintext number back to bytes
        plaintext = plaintext_number.to_bytes((plaintext_number.bit_length() + 7) // 8, byteorder="big")
        return plaintext

# Given values
n = 3133727889560623279067449050415883363161841363809839353437220313773692893737034624474737881355120420202586943633712217730116572074049424194899552073241493
e = 31337
c = 505138831291343697414258349805545490137932579820032124660778458996726516794068227316006233745474187509058323816277752465103889204919145441559038854591269

# Decrypt the message
decrypted_message = RSA.decrypt_prime_n(c, e, n)
print("Decrypted message:", decrypted_message.decode(errors="replace"))
