from datetime import datetime, timedelta

w = input()
a, b, c = map(int, w.split('/'))

if a % b == 0 and (a / b) % c == 0:
    print(w)
    exit(0)

d = datetime.strptime(w, '%Y/%m/%d')

while True:
    d = d + timedelta(days=1)
    str_d = d.strftime('%Y/%m/%d')
    a, b, c = map(int, str_d.split('/'))

    if a % b == 0 and (a / b) % c == 0:
        print(str_d)
        exit(0)
