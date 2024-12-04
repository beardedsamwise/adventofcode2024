"""Day 2: Red-Nosed Reports"""

from aocd import get_data

data = get_data(day=2, year=2024).splitlines()

list_of_data = []

for line in data:
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    list_of_data.append(line)

safe_reports = 0

for line in list_of_data:

    sorted_line = line.copy()
    sorted_line.sort()

    reverse_line = line.copy()
    reverse_line.sort(reverse=True)

    line_length = len(line)
    unique_items = len(set(line))

    if (line == sorted_line or line == reverse_line) and line_length == unique_items:

        SAFE = True

        for i in range(len(sorted_line) - 1):
            diff = int(sorted_line[i + 1]) - int(sorted_line[i])
            if diff > 3:
                SAFE = False

        if SAFE:
            safe_reports += 1

print(safe_reports)
