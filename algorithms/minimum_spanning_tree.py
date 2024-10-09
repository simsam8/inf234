"""
Input: G (V,E), l = E -> Natural numbers

Ouput: A spanning tree T = (V,C) with l(E') smallest possible

Algorithm(Prim's):

Let S = empty
c(v) = infitite for all v
c(s) = 0 for some s in V

while S != V:
    pick v in V-S with smallest c value
    S <- S union {v}
    for u in Neighbors(v) - S :
        if l(vu) < c(u):
            c(u) = l(vu)
            pre(u) = v

return pre


Algorithm(Kruskal's):

E = sorted(E)
let T=(empty set)
for each edge e in E:
    if T + e is still a forest:
        add e to T
"""
