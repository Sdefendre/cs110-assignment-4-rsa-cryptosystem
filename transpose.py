import stdarray
import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    a = stdarray.create2D(m, n)
    for i in range(m):
        for j in range(n):
            a[i][j] = stdio.readFloat()
    c = _transpose(a)
    for row in c:
        for v in row:
            stdio.write(str(v) + " ")
        stdio.writeln()

# Returns the transpose of a.
def _transpose(a):
    m = len(a)
    n = len(a[0])
    t = stdarray.create2D(n, m)
    for i in range(m):
        for j in range(n):
            t[j][i] = a[i][j]
    return t

if __name__ == "__main__":
    main()
