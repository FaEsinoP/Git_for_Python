word = input().replace(" ", "")
my_list = []
my_tmp_list = []
my_tmp_list.append(word[0])
for bukva in range(1, len(word)):
    if word[bukva] == word[bukva - 1]:
        my_tmp_list.append(word[bukva])
    else:
        my_list.append(my_tmp_list.copy())
        my_tmp_list.clear()
        my_tmp_list.append(word[bukva])
    if bukva == len(word) - 1:
       my_list.append(my_tmp_list.copy())
print(my_list)
