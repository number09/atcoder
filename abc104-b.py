str_s = input()

if str_s[0] != 'A':
    print("WA")
    exit(0)

if str_s[2:-1].count("C") != 1:
    print("WA")
    exit(0)

idx_c = str_s.find("C")

w_str = str_s[1:idx_c] + str_s[idx_c +1:]
if w_str.islower():
    print("AC")
else:
    print("WA")





