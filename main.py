def number_of_pairs(gloves):
    arr = {}
    count = 0
    for i in range(len(gloves)):
        for j in range(i, len(gloves)):
            if gloves[i] == gloves[j]:
                count += 1
        if gloves[i] not in arr:
            arr[gloves[i]] = count
        count = 0
    for i in arr:
        count += arr[i] // 2
    return (count)
