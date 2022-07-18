lst = [input() for _ in range(int(input()))]

d1 = {}
for i in lst:
    a, b, c = i.split()[0], i.split()[1], int(i.split()[2])
    if a not in d1:
        d1[a] = d1.setdefault(a, {b: c})
    else:
        if b not in d1[a]:
            d1[a].update({b: c})
        else:
            d1[a][b] = d1[a].get(b) + c

for bigKeys, bigValues in sorted(d1.items()):
    print(bigKeys + ":")
    for keys, values in sorted(bigValues.items()):
        print(keys, values)
