from itertools import chain
from random import randrange

"""
Input:
A set of intervals I={(s1,f1),...,(sn,fn)}

Output:
Partition I into fewest possible pairwise non-overlapping intervals


Algoritm O(nlogn):
WLOG. Assume all timesteps are unique

Compute depth(I) = N_c, max overlap of intervals

Create a stack of N_c available colors.

Create a list of sorted intervals(start and endpoints).

For each timestep t:
    if I starts at t:
        c = pop color -> I
    if I ends at t:
        push back its color on the stack


"""


def generate_intervals(n_intervals, max_range):
    intervals = []
    for _ in range(n_intervals):
        start = randrange(0, max_range)
        end = randrange(start + 1, max_range + 1)
        intervals.append([start, end])

    return intervals


def interval_partitioning(intervals):
    # colors = []
    # timestamps = sorted(list(set(chain.from_iterable(intervals))))
    intervals.sort(key=lambda x: x[1])
    for interval in intervals:
        print(interval)


def main():
    intervals = generate_intervals(3, 10)
    interval_partitioning(intervals)


if __name__ == "__main__":
    main()
