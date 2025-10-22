"""
Independent Set (NP-hard)

Input: Graph G=(V,E)

Output:
A maximum independent set S subset of V,
meaning S is pairwise non-adjacent.

Weighted Independent Set on trees:

Idea: Dynamic programming on rooted subtrees

Let r be the root of T
Let T_v be the subtree rooted in V


            two values
DP[T_v] = optimal solution for subtree rooted in v
            if v is in the solution and if v is out of solution

BASE CASE:
OPT[T_l] = (in=weight(l), out=0) where l is a leaf

RECURSIVE STEP:
DP[T_v] = (
        in=weight(v) + DP[T_u1].out + DP[T_u2].out,
        out = max(DP[T_u1].in, DP[T_u1].out) + max(DP[T_u2].in, DP[T_u2].out)
        )

Must be computed in post-order!!

The optimum solution is max(DP[T].in, DP[T].out)
"""
