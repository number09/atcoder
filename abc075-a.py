ls = list(input().split())


print(sorted(ls, key=lambda x: ls.count(x))[0])


