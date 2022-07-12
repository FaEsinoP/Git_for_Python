n = int(input())
matrix = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            if i == j and j < n - k and i < n - k:
                matrix[i + k][j] = k
                matrix[i][j + k] = k
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()