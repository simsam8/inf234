"""
Counting Inversions

Input: list of integers L
Output: number of pairs that are inverted: i,j, such that i < j but L[i] > L[j]

T(n) = 2T(n/2) + O(n)
-> O(nlogn)

def sort_and_count(L):
    if len(L) <= 1: return (0, L)

    inv1, L1 = sort_and_count(L[:len(L)//2])
    inv2, L2 = sort_and_count(L[len(L)//2:])

    p1, p2 = 0

    L = []

    count = 0

    while p1 < len(L1) and p2 < len(L2):
        if L1[p1] < L2[p2]:
            L.append(L1[p1])
            p1 += 1
        else:
            count += len(L1) - p1
            L.append(L2[p2])
            p2 += 1
    return (inv1 + inv2 + count, L + L1[p1:] + L2[p2:])
"""


def sort_and_count(L):
    if len(L) <= 1:
        return (0, L)

    inv1, L1 = sort_and_count(L[: len(L) // 2])
    inv2, L2 = sort_and_count(L[len(L) // 2 :])

    p1, p2 = 0, 0

    L = []

    count = 0

    while p1 < len(L1) and p2 < len(L2):
        if L1[p1] < L2[p2]:
            L.append(L1[p1])
            p1 += 1
        else:
            count += len(L1) - p1
            L.append(L2[p2])
            p2 += 1
    return (inv1 + inv2 + count, L + L1[p1:] + L2[p2:])


print(sort_and_count([3, 7, 10, 14, 2, 11, 16, 18]))
