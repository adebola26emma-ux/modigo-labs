def build_roster(students):
    roster = {}
    # TODO: loop through `students` and group names by grade in `roster`
    for name, grade in students:
        if grade not in roster:
            roster[grade] = []
        check = True
        for gradex in roster:
            if name in roster[gradex]:
                check = False
        if check: # Checks if the student exists in a different grade   
            roster[grade].append(name)
    return roster

print(build_roster([('ADa', 5), ('Bola', 6), ('Chidi', 5), ('ADa', 6)]))