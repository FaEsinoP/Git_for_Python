def spin_words(sentence):
    arr = sentence.split(" ")
    new = []
    for word in arr:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string
