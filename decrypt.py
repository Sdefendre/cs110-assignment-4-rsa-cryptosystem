import rsa
import stdio
import sys

# Entry point.
def main():
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    width = rsa.bitLength(n)
    bits = stdio.readAllStrings()
    for i in range(0, len(bits), width):
        chunk = ""
        for j in range(width):
            chunk += bits[i + j]
        value = rsa.bin2dec(chunk)
        stdio.write(chr(rsa.decrypt(value, n, d)))

if __name__ == "__main__":
    main()
