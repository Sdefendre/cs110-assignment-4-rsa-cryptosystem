import rsa
import stdio
import sys

# Entry point.
def main():
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    width = rsa.bitLength(n)
    text = stdio.readAll()
    for ch in text:
        bits = rsa.dec2bin(rsa.encrypt(ord(ch), n, e), width)
        for bit in bits:
            stdio.writef("%s ", bit)
    stdio.writeln()

if __name__ == "__main__":
    main()
