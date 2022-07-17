secret = input()
dict_secret = {}
for i in secret:
    dict_secret[i] = dict_secret.get(i, 0) + 1

mydict = {}
n = int(input())
for _ in range(n):
    key, value = input().split(": ")
    mydict[key] = value
answer = ""
for i in range(len(secret)):
    for key, value in dict_secret.items():
        for key2, value2 in mydict.items():
            if int(value2) == value:
                if secret[i] == key:
                    answer += key2
print(answer)
