from random import randrange

"""
Interval Scheduler

Input:
A set of intervals I={(s1,f1),...,(sn,fn)}

Output:
A maximum size set of pairwise non-overlapping intervals

Solution: Greedy algorithm


Algorithm:
Let R be the input intervals
    Sort R by finish time
    Let A = {}
    while R is not empty:
        pick the first I in R
        add I to A
        remove conflicting intervals from R

    return A
"""


def interval_scheduler(intervals: list[tuple]):
    intervals.sort(key=lambda x: x[1])
    A = [intervals[0]]

    for interval in intervals:
        if interval[0] >= A[-1][1]:
            A.append(interval)

    return A


def generate_intervals(n_intervals, max_range):
    intervals = []
    for _ in range(n_intervals):
        start = randrange(0, max_range)
        end = randrange(start + 1, max_range + 1)
        intervals.append((start, end))

    return intervals


def main():
    intervals = generate_intervals(5, 10)
    print("Input Intervals")
    print(intervals)
    solution = interval_scheduler(intervals)
    print("Solution")
    print(solution)


if __name__ == "__main__":
    main()
