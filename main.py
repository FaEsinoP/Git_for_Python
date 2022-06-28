def indexedSequentialSearch(arr, n, k):
    elements = [0] * 20
    indices = [0] * 20

    ind = 0

    for i in range(0, n, 3):
        # Элемент хранения

        elements[ind] = arr[i]

        # Хранение индекса

        indices[ind] = i

        ind += 1

    if k < elements[0]:

        print("Not found")

        exit(0)

    else:
        for i in range(1, ind + 1):
            if k < elements[i]:
                start = indices[i - 1]
                end = indices[i]
                break

    for i in range(start, end + 1):
        if k == arr[i]:
            print("Found at index", i)
            break


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    k = 4

    indexedSequentialSearch(arr, n, k)
