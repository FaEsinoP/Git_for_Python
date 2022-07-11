n = 8
doska = [['.'] * n for _ in range(n)]
k = list(input())
if k[0] == "a":
    k[0] = 0
if k[0] == "b":
    k[0] = 1
if k[0] == "c":
    k[0] = 2
if k[0] == "d":
    k[0] = 3
if k[0] == "e":
    k[0] = 4
if k[0] == "f":
    k[0] = 5
if k[0] == "g":
    k[0] = 6
if k[0] == "h":
    k[0] = 7
doska[n - int(k[1])][int(k[0])] = "N"
nomer, bukva = n - int(k[1]), int(k[0])

for i in range(n):
    for j in range(n):
        if i == nomer - 2 and ((j == bukva + 1) or (j == bukva - 1)):
            doska[i][j] = "*"
        if i == nomer + 2 and ((j == bukva + 1) or (j == bukva - 1)):
            doska[i][j] = "*"
        if i == nomer - 1 and ((j == bukva + 2) or (j == bukva - 2)):
            doska[i][j] = "*"
        if i == nomer + 1 and ((j == bukva + 2) or (j == bukva - 2)):
            doska[i][j] = "*"
for i in range(n):
    for j in range(n):
        print(doska[i][j], end=" ")
    print()
