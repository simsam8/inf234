"""
Max flow

Input: flow network

Out: A flow with maximum value

Algorithm (Greedy)

P -> augmenting path

while P:= s-t-path with positive bottleneck
    then for e in P:
        f(c) += b

return f


Residual graph

Given a flow network G, s, t, c, and a flow f
The residual graph is the graph with the same vertex set,
and for each edge uv in E(G), we create 2 edges
uv with capacity C(uv) - f(uv)
vu with capacity f(uv)

Algorithm(Ford-Falkerson 55)
Runtime O(m*F) where F is the max flow

Let f_e <- 0 for all e in E(g)
Do:
    Find an s-t-path in G_f
    Let b <- bottleneck of P
    For each edge e = (uv) in P
        if e is a forward edge: <==> 'is e in G?'
            f_e += b
        else (it is a backwards edge)
            let e' = vu
            f_e' -= b

return f
"""
