# RSA Cryptosystem

A from-scratch RSA implementation in Python: key generation, encryption and decryption, plus command-line programs that chain together with pipes.

## What it does

- **`rsa.py`**: the library. It generates primes in a range, picks two distinct primes `p` and `q`, computes `n = pq` and Euler's totient, chooses a public exponent `e` coprime to the totient, and derives the private exponent `d` as its modular inverse. Encryption and decryption use modular exponentiation.
- **`keygen.py`**, **`encrypt.py`**, **`decrypt.py`**: command-line drivers that read standard input and write standard output.

```sh
python3 keygen.py 50 100                       # prints: n e d
python3 encrypt.py <n> <e> < message.txt > secret.txt
python3 decrypt.py <n> <d> < secret.txt         # prints the original text
```

I tested that the round trip `decrypt(encrypt(x))` returns the original text.

## Concepts

Number theory (primes, totients, modular inverses), modular exponentiation, and Unix-style programs composed with pipes.

Also included are warm-up exercises: `reverse`, `distance`, `transpose`, `palindrome` and `sin`.

## Running it

These programs use the standard libraries from *Introduction to Programming in Python* (Sedgewick, Wayne & Dondero): `stdio`, `stdarray`, `stdrandom` and friends. Put those modules on your `PYTHONPATH`, then run the scripts with Python 3.

## Course

CS110 Introduction to Computing, UMass Boston, Spring 2026 (instructor: Swami Iyer). The instructor supplied the starter code and course libraries. My approach and notes for each problem are in [`notes.txt`](notes.txt).
