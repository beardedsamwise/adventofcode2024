"""Day 3: Mull It Over"""

import re

from aocd import get_data

data = get_data(day=3, year=2024)

# part 1

results = re.findall(r"\W*(mul)\W*(\d+,\d+)\)", data)

tally = 0

for calc in results:
    values = calc[1].split(",")
    tally += int(values[0]) * int(values[1])

print(tally)

# part 2

r = re.compile(r"(don't\(\)|do\(\))|\W*mul\W*(\d+,\d+)\)")  # |(do())
results = r.findall(data, re.MULTILINE)

tally = 0

ENABLED = True

for calc in results:
    if calc[0] == "don't()":
        ENABLED = False
    if calc[0] == "do()":
        ENABLED = True
    if ENABLED:
        if calc[1]:
            values = calc[1].split(",")
            tally += int(values[0]) * int(values[1])

print(tally)
