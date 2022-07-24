with open(input(), 'r', encoding="utf-8") as f:
    definition = []
    file = f.readlines()
    for i in range(len(file)):
        if file[i][:4] == 'def ' and (i == 0 or file[i - 1][0] != '#'):
            definition.append(file[i][4:file[i].find('(')])

    for i in definition:
        print(i)
    if len(definition) == 0:
        print("Best Programming Team")
