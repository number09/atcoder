n = int(input())
wkday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

li_input = list()

for _ in range(n):
    li_input.append(input())

for w in li_input:
    new_idx = int((wkday.index(w) + 1) % 7)
    print(wkday[new_idx])

