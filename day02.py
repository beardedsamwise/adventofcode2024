"""Day 2: Red-Nosed Reports"""

from aocd import get_data

data = get_data(day=2, year=2024).splitlines()

safe_reports = 0

for line in data:
    # print(line)
    split_line = line.split()

    sorted_line = split_line.copy()
    sorted_line.sort()

    reverse_line = split_line.copy()
    reverse_line.sort(reverse=True)

    line_length = len(split_line)
    unique_items = len(set(split_line))

    if (
        split_line == sorted_line or split_line == reverse_line
    ) and line_length == unique_items:
        # print(line)
        # print(sorted_line)
        SAFE_REPORT = True
        for i in range(len(split_line) - 1):
            # print("----")
            # print(sorted_line[i + 1])
            # print("MINUS")
            # print(sorted_line[i])
            # print("")
            if int(sorted_line[i + 1]) - int(sorted_line[i]) > 3:
                SAFE_REPORT = False
        if not SAFE_REPORT:
            print(f"Unsafe report: {line}")
        else:
            print(f"SAFE report: {line}")
            safe_reports += 1


print(safe_reports)
