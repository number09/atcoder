a = int(input())
b = int(input())


print(list(set(range(1, 4)).difference(set([a, b])))[0])
