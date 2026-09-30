def has_conflict(meetings):
    # TODO: return True if any two meetings overlap in time, False otherwise
    for i in range(len(meetings)):
        for j in range(i+1, len(meetings)):
            if meetings[j][0] < meetings[i][1]:
                return True

    return False

print(has_conflict([(1, 3), (2, 4)]))
print(has_conflict([(1, 3), (3, 5)]))
print(has_conflict([]))
print(has_conflict([(5, 6), (1, 10)]))
