s = input()

now = ""
counter = 0
for w in s:
    if now != w:
        counter += 1
    now = w

print(counter - 1)

