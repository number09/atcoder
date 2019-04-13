s = list(input())

now = 0
end = len(s)

while now < end:
    if s[now] == 'W' and now != (len(s) - 1) and s[now + 1] == 'A':
        s[now] = 'A'
        s[now + 1] = 'C'
        if now != 0:
            now -= 1
        else:
            now += 1
    else:
        now += 1


print("".join(s))


