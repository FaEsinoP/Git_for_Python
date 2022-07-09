arr = input().split()
result = [[]]
for i in range(1, len(arr)+1):
    for j in range(len(arr)):
        if j == 0:
            result.append(list(arr[j:i * 1]))
        elif len(list(arr[j:i + j])) == i:
            result.append(list(arr[j:i + j]))
print(result)