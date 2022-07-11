matrix = []
sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0

n = int(input())

for i in range(n):
    matrix.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(n):
        if j < i > n - j - 1:
            sum_3 += matrix[i][j]
        if j < i < n - j - 1:
            sum_2 += matrix[i][j]
        if j > i > n - j - 1:
            sum_4 += matrix[i][j]
        if j > i < n - j - 1:
            sum_1 += matrix[i][j]
print("Верхняя четверть:", sum_1)
print("Правая четверть:", sum_4)
print("Нижняя четверть:", sum_3)
print("Левая четверть:", sum_2)