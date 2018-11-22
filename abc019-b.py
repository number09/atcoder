s = input()

li = list()
for w in s:
    if len(li) == 0 or li[-1][0] != w:
        li.append([w, 1])
    else:
        li[-1][1] += 1

temp_list = list()
for x in li:
    temp_list.append(''.join(map(str, x)))
print(''.join(temp_list))
