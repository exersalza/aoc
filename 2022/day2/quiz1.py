# first column: A: Rock, B: Paper, C: Scissors
# Second column: X: Rock, Y: Paper, Z: Scissors

# Scores: Rock: 1, Paper: 2, Scissors: 3
# Lost: 0, Draw: 3, Win: 6

t = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
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
        p2 = t[line[2]]

        if p1 == p2:
            total_score += (p2 + 3)
            continue

        if b[p1] == p2:
            total_score += p2
            continue

        if b[p1] != p2:
            total_score += (p2 + 6)
            continue

print(total_score)
