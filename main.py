def sort_array(source_array):
    sch = 0
    nechet = [i for i in source_array if i % 2 == 1]
    nechet.sort()
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = nechet[sch]
            sch += 1
    return source_array
