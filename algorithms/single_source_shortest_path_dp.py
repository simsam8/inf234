"""
Shortest path

Input: Digraph G=(V, E) w: E -> integers, source(s) in V

Out: dist(s,v) for all v in V
        or a negative cycle

DP[i, v] = cost of shortest s-v-path using at most i edges.

BASE CASE:
DP[0, v] = {0 if v=s else inf}

RECURSIVE STEP:
DP[i, v] = min( min_u_neighbor(v) DP[i-1, u]+w(u,v),
                DP[i-1, v]) in case there is a shortest path using <= i-1 edges

In Code:

dist(s,t) = DP[n-1, t]

DP = defaultdict(lambda, inf)

DP[0, s] = 0

for i in range(1,n):
    for v in V:
        DP[i,v] = DP[i-1, v]
        for u in neighbor(v):
            cost = DP[i-1, u] + w(u,v)
            if cost < DP[i,v]:
                DP[i,v] = cost
                pre[v] = u

we can find the cycle by traversing pre from the
vertex that created in column n.
"""
