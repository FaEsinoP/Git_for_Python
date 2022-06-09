def duplicate_count(text):
    slovar = {}
    count = 0
    count_all = 0
    for i in text:
        for j in text:
            if j.lower() == i.lower():
                count += 1
        if i.lower() not in slovar:
            slovar[i.lower()] = count
        count = 0
    for i in slovar:
        if slovar[i] > 1:
            count_all += 1
    return count_all
    pass
