"""Day 1: Historian Hysteria"""

from aocd import get_data

data = get_data(day=1, year=2024).splitlines()

# PART 1

first_list = []
second_list = []

for i, line in enumerate(data):
    line = line.split()
    first_list.append(int(line[0]))
    second_list.append(int(line[1]))

first_list.sort()
second_list.sort()

totals = 0

for i in range(len(first_list)):
    if first_list[i] > second_list[i]:
        totals += first_list[i] - second_list[i]
    else:
        totals += second_list[i] - first_list[i]

print(totals)

# PART 2

unique_nums = set(first_list)
totals = 0

for num in unique_nums:
    appearances = second_list.count(num)
    totals += num * appearances

print(totals)
