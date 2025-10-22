"""
Knapsack
v is value, w is weight
Input: A={(v1, w1), ..., (vn, wn)}
W in natural numbers

Question:
Compute a set A' subset A such that the sum of values are maximized
constrained to that the sum of weights <= W


Algorithm:

OPT(i, w) = maximum value we can get using items 1 .. i,
            weighing at most w

base case:

OPT(0, w) = 0 for all 0 <= w <= W

recursive step:
OPT(i, w) = max(OPT(i-1, w-wi) + vi, # given that w>=wi
                OPT(i-1, w))
"""

W = 20

example = [(500, 5.5), (6, 2), (18, 5), (22, 5), (30, 7)]


def knapsack(items):
    items.insert(0, (0, 0))
    n = len(items)
    OPT = {}
    for i in range(n):
        v_i = items[n][0]
        w_i = items[n][1]
        for w in range(W + 1):
            if i == 0:
                OPT[(0, w)] = 0
            else:
                OPT[(i, w)] = max(OPT[(i - 1, w - w_i)] + v_i, OPT[(i - 1, w)])

    return OPT[n, W]


print(knapsack(example))
