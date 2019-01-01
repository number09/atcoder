s = input()
x = 753
print(min(abs(x - int(s[i:i + 3])) for i in range(len(s) - 2)))
