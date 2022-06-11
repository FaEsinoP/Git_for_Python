def in_array(array1, array2):
    arr = []
    for i in array1:
        for j in array2:
            if i not in arr and i in j:
                arr.append(i)
    arr.sort()
    return arr
