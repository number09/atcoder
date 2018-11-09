s = input()
n = int(input())
print([x + y for x in s for y in s][n - 1])
