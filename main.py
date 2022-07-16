n = int(input())
arr = []
for i in range(n):
    myset = set()
    for j in range(int(input())):
        myset.add(input())
    arr.append(myset)
for i in arr:
    arr[0].intersection_update(i)
for i in sorted(arr[0]):
    print(i)