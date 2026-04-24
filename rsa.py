import math
import stdio
import stdrandom
import sys

# Generates and returns the public/private keys as a tuple (n, e, d). Prime 
# numbers p and q needed to generate the keys are picked from the 
# interval [lo, hi).
def keygen(lo, hi):
    primes = _primes(lo, hi)
    p, q = _sample(primes, 2)
    n = p * q
    m = (p - 1) * (q - 1)
    candidates = []
    for prime in _primes(2, m):
        if m % prime != 0:
            candidates += [prime]
    e = _choice(candidates)
    d = 1
    while (e * d) % m != 1:
        d += 1
    return n, e, d

# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return pow(x, e, n)

# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return pow(y, d, n)

# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2

# Returns the binary representation of n expressed in decimal, having the 
# given width, and padded with leading zeros.
def dec2bin(n, width):
    return format(n, "0%db" % (width))

# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)

# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    if hi <= 2 or hi <= lo:
        return []
    sieve = [True] * hi
    if hi > 0:
        sieve[0] = False
    if hi > 1:
        sieve[1] = False
    i = 2
    while i * i < hi:
        if sieve[i]:
            j = i * i
            while j < hi:
                sieve[j] = False
                j += i
        i += 1
    primes = []
    start = lo
    if start < 2:
        start = 2
    for i in range(start, hi):
        if sieve[i]:
            primes += [i]
    return primes

# Returns a list containing a random sample (without replacement) of k items 
# from the list a.
def _sample(a, k):
    copy = a[:]
    sample = []
    for i in range(k):
        index = stdrandom.uniformInt(0, len(copy))
        sample += [copy[index]]
        del copy[index]
    return sample

# Returns a random item from the list a.
def _choice(a):
    index = stdrandom.uniformInt(0, len(a))
    return a[index]

# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))

if __name__ == "__main__":
    _main()
