def binary_search(A: list, item):
    height = len(A)
    low = 0
    while height >= low:
        mid = (height + low) // 2
        if A[mid] == item:
            return mid
        if A[mid] > item:
            height = mid - 1
        else:
            low = mid + 1
    return None


A = [10, 20, 30, 40, 54]

print(binary_search(A, 40))
