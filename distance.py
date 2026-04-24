import math
import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    n = int(sys.argv[1])
    x, y = [], []
    for i in range(n):
        x += [stdio.readFloat()]
    for i in range(n):
        y += [stdio.readFloat()]
    stdio.writeln(_distance(x, y))

def _distance(x, y):
    total = 0.0
    for i in range(len(x)):
        diff = x[i] - y[i]
        total += diff * diff
    return math.sqrt(total)

if __name__ == "__main__":
    main()
