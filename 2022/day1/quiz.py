""" Question
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:
they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

https://adventofcode.com/2022/day/1
"""

i = []
temp = []
out = []

with open("input", "r") as f:
    for line in f:
        if line == "\n":
            i.append([j for j in temp])
            temp.clear()
            continue

        temp.append(int(line.replace("\n", "")))


for j in i:
    out.append(sum(j))

out.sort(reverse=True)

# Answer of part 1:
print("Answer to part 1: ", out[0])

# Answer to part 2:
print("Answer to part 2: ", sum(out[0:3]))
