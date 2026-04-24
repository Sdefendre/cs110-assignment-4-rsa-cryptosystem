import math
import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    x = float(sys.argv[1])
    stdio.writeln(_sin(math.radians(x)))

# Returns sin(x) calculated using the formula: sin(x) = x - x^3/3! + x^5/5! - 
# x^7/7! + ...
def _sin(x):
    term = x
    total = 0.0
    i = 1
    while abs(term) > 1e-15:
        total += term
        term *= -1 * x * x / ((2 * i) * (2 * i + 1))
        i += 1
    return total

if __name__ == "__main__":
    main()
