m = int(input())

vv = '00'
if m < 100:
    vv = '00'
elif 100 <= m <= 5000:
    vv = format(int(m / 1000 * 10), '02')
elif 6000 <= m <= 30000:
    vv = format(int(m / 1000 + 50), '02')
elif 35000 <= m <= 70000:
    vv = format(int((m / 1000 - 30) / 5 + 80), '02')
else:
    vv = '89'

print(vv)
