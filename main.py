chislo = input()
arr = list(chislo)
numbers = arr[-5:]
numbers.reverse()
answer = []
if len(arr) == 5:
    arr = []
else:
    arr = arr[0]

for i in range(len(arr)):
    answer.append(arr[i])
for i in range(len(numbers)):
    answer.append(numbers[i])
while answer[0] == str(0):
    answer.pop(0)
print("".join(answer))
