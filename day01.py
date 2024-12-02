"""Day 1: Historian Hysteria"""

from aocd import get_data

data = get_data(day=1, year=2024).splitlines()

first_list = []
second_list = []

for i in range(len(data)):
    first_list.append(data[i].split()[0])
    second_list.append(data[i].split()[1])

print(first_list)
print(second_list)
