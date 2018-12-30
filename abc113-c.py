n, m = map(int, input().split())
li_input = list()
counter = dict()
cities = dict()

for i in range(m):
    li_input.append(list(map(int, input().split())))

sorted_city = sorted(li_input, key=lambda x: x[1])

for c in sorted_city:
    idx = counter.get(c[0], 0)
    cities[c[1]] = idx

    # count up
    counter[c[0]] = idx + 1


for c in li_input:
    print('{0:06}{1:06}'.format(c[0], cities[c[1]] + 1))

