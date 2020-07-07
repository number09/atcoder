n = int(input())
d_count = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

for i in range(n):
    w = input()
    d_count[w] = d_count[w] + 1

print('AC x ' + str(d_count['AC']))
print('WA x ' + str(d_count['WA']))
print('TLE x ' + str(d_count['TLE']))
print('RE x ' + str(d_count['RE']))
