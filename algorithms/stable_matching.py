import random

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


def main():
    n_pairs = 10
    hospitals = {f"h{n}" for n in range(n_pairs)}
    students = {f"s{n}" for n in range(n_pairs)}
    hospital_prefs = {
        hospital: random.sample(sorted(students), n_pairs) for hospital in hospitals
    }
    student_prefs = {
        student: random.sample(sorted(hospitals), n_pairs) for student in students
    }

    print("\nHospital preferences:")
    for hosp, prefs in hospital_prefs.items():
        print(f"{hosp}: {prefs}")

    print("\nStudent preferences:")
    for stud, prefs in student_prefs.items():
        print(f"{stud}: {prefs}")

    matchings = stable_matching(hospitals, students, hospital_prefs, student_prefs)
    print("\nOutput:")
    for h, s in matchings.items():
        print(f"{h}:{s}")


if __name__ == "__main__":
    main()
