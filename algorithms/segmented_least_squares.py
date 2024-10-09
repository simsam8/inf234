"""
Segmented Least Squares

Input: (x_1, y_1), ..., (x_n, y_n)
Output: A segmentation (contiguos partition) S_1, S2, ..., S_t

such that c*t + sum_i=1->t(errore(Si)) is minimized

solution: opt[n] = min_j<n{c+error(pj,pj+1,...,pn) + opt[j-1]}
"""
