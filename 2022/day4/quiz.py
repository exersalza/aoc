o = 0
fo = 0

with open("input", 'r') as f:
    for line in f:
        t1, t2 = line.strip().split(',')
        a, a1 = map(int, t1.split('-'))
        b, b1 = map(int, t2.split('-'))

        o1 = max(a, b)
        o2 = min(a1, b1)

        if o1 <= o2:
            # get full overlap
            if o1 == a and o2 == a1 or \
                    o1 == b and o2 == b1:
                fo += 1

            # get overlap
            o += 1

print(o, fo)
