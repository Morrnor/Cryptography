import primes

class LCGPseudoRandomGenerator:
    def __init__(self, a=48271, c=0, m=2**31-1, seed=None):  
        self.a = a  # Multiplicative factor
        self.c = c  # Increment
        self.m = m  # Modulus

        # If no seed is provided, it generates a pseudo-random seed based on object id
        if seed is None:
            self.x0 = int((6364136223846793005 * hash(str(id(self)))) & 0xFFFFFFFFFFFFFFFF)
        else:
            self.x0 = seed

        # Initializing the previous state of the generator.
        self.x_prev = (self.a * self.x0 + self.c) % self.m
    
    # Method to generate a pseudo-random number using the LCG algorithm.
    def generate_number(self, num_range=None):
        self.x_prev = (self.a * self.x_prev + self.c) % self.m

        # Scaling the number to fit within a specific range if num_range is provided.
        if num_range is None:
            return self.x_prev
        else:
            return int((self.x_prev / (self.m - 1)) * (num_range[1] - num_range[0]) + num_range[0])

class RSA:
    def __init__(self):
        pass

    @staticmethod
    def generate_pq():
        # Selecting the first prime number from the list based on a generated index.
        p = primes.primes_list[lcg.generate_number([0, 3783])]
        # Selecting the second prime number from the list based on another generated index.
        q = primes.primes_list[lcg.generate_number([0, 3783])]
        return p, q

    # Function to calculate n from p and q
    @staticmethod
    def calculate_n(p, q):
        return p * q

    # Function to calculate Euler's totient function for n from p and q
    @staticmethod
    def calculate_phi_n(p, q):
        return (p - 1) * (q - 1)

    # Function to find the greatest common divisor of two numbers
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Function to calculate e
    @staticmethod
    def calculate_e(phi_n):
        e = 2
        while True:
            if e < phi_n and RSA.gcd(e, phi_n) == 1:  
                break
            e += 1
        return e

    # Function to find the modular multiplicative inverse of "e" mod phi_n
    @staticmethod
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, x, y = RSA.extended_gcd(b % a, a)
            return (gcd, y - (b // a) * x, x)

    # Function to calculate d
    @staticmethod
    def calculate_d(e, phi_n):
        gcd, x, y = RSA.extended_gcd(e, phi_n)
        return x % phi_n

     # Function to encrypt plaintext using public key (e, n)
    @staticmethod
    def encrypt(plaintext, e, n):
        # Encrypt each character in plaintext using modular exponentiation 
        # Converts each char to its Unicode point where the chars Unicode point is raised to the power of "e" modulo "n"
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext

    # Function to decrypt ciphertext using private key (d, n)
    @staticmethod
    def decrypt(ciphertext, d, n):
        # Decrypt each character in ciphertext using modular exponentiation
        # Converts each char to its Unicode point where the chars Unicode point is raised to the power of "d" modulo "n"
        plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
        return plaintext


# Creating an instance of the LCGPseudoRandomGenerator class.
lcg = LCGPseudoRandomGenerator()

# Generating p and q using the RSA class
p, q = RSA.generate_pq()

# Calculating n
n = RSA.calculate_n(p, q)

# Calculating Euler's totient function for n.
phi_n = RSA.calculate_phi_n(p, q)

# Calculating e
e = RSA.calculate_e(phi_n)

# Calculating d
d = RSA.calculate_d(e, phi_n)

# Printing the values of p, q, n, e, and d which are used in the RSA encryption algorithm
print("p:", p)
print("q:", q)
print("n:", n)
print("e (Public Key):", e)
print("d (Private Key):", d)

# Example usage of encryption and decryption
message = "Hello, world!"
print("Original message:", message)

encrypted_message = RSA.encrypt(message, e, n)
print("Encrypted message:", encrypted_message)

decrypted_message = RSA.decrypt(encrypted_message, d, n)
print("Decrypted message:", decrypted_message)
