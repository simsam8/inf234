"""
Input Sets H and S, Size of H==S
    and list of preferences

Output a stable perfect matching M

explanation:

Initially noone is matched

while some hospital is unmatched
    and has not yet proposed to all students:

    h proposes to the higehst ranked student s
        that it has not yet proposed to

    if s is unmatched
        add (h,s) to M
    else if s prefers h over its current mathed h'
        replace (h',s) with (h,s)  in M
    else
        s rejects h # do nothing
"""

hosp = {"h1", "h2"}
stud = {"s1", "s2"}

prefs_hosp = {"h1": ["s1", "s2"], "h2": ["s1", "s2"]}

prefs_stud = {"s1": ["h1", "h2"], "s2": ["h1", "h2"]}


def stable_matching(
    hospitals: set, students: set, prefs_hospitals: dict, prefs_students: dict
):

    matched = {}

    while len(hospitals) > 0:
        current_h = hospitals.pop()
        while current_h not in matched.values() and len(prefs_hospitals[current_h]) > 0:
            current_s = students.pop()
            if current_s not in matched.values():
                matched.update({current_s: current_h})
            elif prefs_students[current_s].index(current_h) < prefs_students[
                current_s
            ].index(matched[current_s]):
                hospitals.add(matched[current_s])
                matched[current_s] = current_h

    return matched


matchings = stable_matching(hosp, stud, prefs_hosp, prefs_stud)
print(matchings)
