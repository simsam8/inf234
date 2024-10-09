"""
Single source shortest path

Input: G = (V, E), length: E -> natural numbers, Source vertex s
Output: dist(s, t) for all t in V

Idea: We maintain a set S where we know the correct distance to every v in S
d(v) = dist(s,v)
d'(v) = tentative distance from s to v

Complexity: n vertices, m edges


Algorithm(Dijkstra's):

d'(v) = infity for all v in V //// d' is the currently best known distance
d'(s) = 0
while S != V:
    pick v in V - S (v in V and not in S) with smallest d'(v)
    S <- S union{v}
    d(v) = d'(v)
    for each u in Neighbor(v) - S:
        if d(s, v) + l(vu) < d'(u):
            d'(u) = d(v) + l(vu)
            pre(u) = v //// predecessor of u is v

return d, pre
"""
