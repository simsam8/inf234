"""
Input:
A set of requests I = {(timespan, deadline)}

Task. Assign a start time to each request
such that no two requests overlap and with
L(lateness) = max_i l_i minimized
l_i = max(0, f(i)-d(i))

Solution: Earliest deadline first

Algorithm O(nlogn):

Sort requests by deadline
i.e. d_1 <= d_2 <= .... <= d_n

let now = s_1 = 0

for i = 1 ... n
    assign request i to [now, now+t_i]
    now <- now+t_i
"""


def lateness_scheduling(requests):
    requests.sort(key=lambda x: x[1])
