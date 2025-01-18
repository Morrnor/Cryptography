class RSA:
    def __init__(self):
        pass

     @staticmethod
    def factorize_n(n):
        from sympy import factorint, isprime
        if isprime(n):
            raise ValueError(f"n is prime: {n}")
        factors = factorint(n)  # Returns {prime: exponent}
        primes = list(factors.keys())
        if len(primes) == 2 and all(factors[p] == 1 for p in primes):  # Ensure two distinct primes
            return primes[0], primes[1]
        else:
            raise ValueError(
                f"Factorization failed or n is not a product of exactly two primes: {factors}"
            )


    @staticmethod
    def calculate_phi_n(p, q):
        return (p - 1) * (q - 1)

    @staticmethod
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, x, y = RSA.extended_gcd(b % a, a)
            return (gcd, y - (b // a) * x, x)

    @staticmethod
    def calculate_d(e, phi_n):
        gcd, x, y = RSA.extended_gcd(e, phi_n)
        return x % phi_n

    @staticmethod
    def decrypt(ciphertext, d, n):
        plaintext_number = pow(ciphertext, d, n)
        plaintext = plaintext_number.to_bytes((plaintext_number.bit_length() + 7) // 8, byteorder="big")
        return plaintext

# Given values
n = 3133727889560623279067449050415883363161841363809839353437220313773692893737034624474737881355120420202586943633712217730116572074049424194899552073241493
e = 31337
c = 505138831291343697414258349805545490137932579820032124660778458996726516794068227316006233745474187509058323816277752465103889204919145441559038854591269

# Factor n
p, q = RSA.factorize_n(n)

# Compute phi(n)
phi_n = RSA.calculate_phi_n(p, q)

# Compute the private key d
d = RSA.calculate_d(e, phi_n)

# Decrypt the message
decrypted_message = RSA.decrypt(c, d, n)
print("Decrypted message:", decrypted_message.decode(errors="replace"))
