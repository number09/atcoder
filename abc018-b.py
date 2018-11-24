s = input()
n = int(input())

for i in range(n):
    st, ed = map(int, input().split())
    wk = s[st - 1:ed:]
    rev = wk[::-1]
    s = s[:st - 1] + rev + s[ed:]

print(s)



