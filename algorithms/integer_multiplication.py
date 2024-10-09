"""
Integer Multiplication

Input: A, B
Output: A * B

Assume that |x| == |y| is a power of 2

Karatsuba's algorithm


def M(x,y): n is len(x) = len(y)
    x1, x0 = split x
    y1, y0 = split y

    if n <= 32:
        return digit multiplication

    A = M(x1, y1)
    B = M(x0, y0)
    P = M((x1 + x0), (y1 + y0))
    S = P - A - B
    return A * 2^n + S * 2^n + B


T(n) <= 3T(n/2) + O(n)

O(n^log_2(3)) = O(n^1.59)

"""

