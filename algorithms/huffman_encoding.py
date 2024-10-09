from collections import Counter
from heapq import heapify, heappop, heappush
from pprint import pprint

"""
Huffman encoding

Input: Alphabet S(Sigma), f_sigma frequencies
Out: An encoding of S that minimizes
    the sum of f_sigma * | gamma(sigma)|

Equal to finding a prefix tree minimizing
the sum of frequencies times the depths

Algorithm(nlogn):

Priority Queue Q = {(f_v, v): v in S}

while |Q| >= 2:
    v1, v2 = pop(Q), pop(Q)
    create node v =  (f1 + f2, (v1, v2))
    push(Q, v)

return pop(Q)
"""


def huffman_encoding(freqs):
    Q = [(f, f"'{s}'") for (s, f) in freqs.items()]
    heapify(Q)
    while len(Q) >= 2:
        f1, v1 = heappop(Q)
        f2, v2 = heappop(Q)
        f = f1 + f2
        v = f"({v1},{v2})"
        heappush(Q, (f, v))
    return eval(heappop(Q)[1])


def traverse(T, prefix=""):
    if isinstance(T, str):
        yield (T, prefix)
        return
    yield from traverse(T[0], prefix + "0")
    yield from traverse(T[1], prefix + "1")


if __name__ == "__main__":
    text = "lrchuleoarchueoalrchcrhlrhchhueoallchlrhlh"
    freqs = Counter(text)
    print(freqs)
    T = huffman_encoding(freqs)

    code = {s: c for (s, c) in traverse(T)}
    pprint(code)
