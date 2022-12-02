# first column: A: Rock, B: Paper, C: Scissors
# Second column: X: Rock, Y: Paper, Z: Scissors

# Scores: Rock: 1, Paper: 2, Scissors: 3
# Lost: 0, Draw: 3, Win: 6

t = {
    'A': 1,
    'B': 2,
    'C': 3,
}

b = {
    1: 3,
    2: 1,
    3: 2
}

total_score = 0
with open('input', 'r') as f:

    for line in f:
        p1 = t[line[0]]

        if line[2].upper() == 'Y':
            total_score += (p1 + 3)

        if line[2].upper() == 'Z':
            for k, v in b.items():
                if v == p1:
                    total_score += (k + 6)

        if line[2].upper() == 'X':
            total_score += (b[p1])


print(total_score)
