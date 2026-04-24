import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))

# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    lo = 0
    hi = len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True

if __name__ == "__main__":
    main()
