s, t = input().split()

if s[0] == t[0] == 'B':
    print(abs(int(s[1]) - int(t[1])))
elif s[1] == t[1] == 'F':
    print(abs(int(s[0]) - int(t[0])))
else:
    w_b = int(s[1]) if s[0] == 'B' else int(t[1])
    w_f = int(s[0]) if s[1] == 'F' else int(t[0])
    print(w_b - 1 + w_f)
