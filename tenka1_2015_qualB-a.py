li = [100, 100, 200]

while len(li) != 20:
    li.append(sum(li[-3:]))
print(li[-1])
