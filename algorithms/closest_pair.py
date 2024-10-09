"""
Closest Pair

Input: Set of points in the plane
Output: A pair with minimum distance

T(n) <= 2T(n/2) + O(n) -> O(nlogn)

def closest_pair(P)
    "assume P sorted by x-coordinates"

    L = P[:n/2]
    R = P[n/2:]

    d_L = closest_pair(L)
    d_R = closest_pair(R)
    d = min(d_L, d_R)

    S = {all pairs <= d away from x*}
    for i in range(len(S)):
        F = S[i:i+8]
        bruteforce(F)
"""
