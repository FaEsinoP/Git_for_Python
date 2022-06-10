def solution(s):
    arr = []
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            arr.append(s[i] + s[i + 1])
    else:
        for i in range(0, len(s), 2):
            if i == len(s) - 1:
                arr.append(s[i] + "_")
            else:
                arr.append(s[i] + s[i + 1])

    return arr
