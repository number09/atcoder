str_s = input()

all = set([chr(i) for i in range(97, 97+26)])
inputs = set(list(str_s))

diff = all.difference(inputs)

if len(diff) > 0:
    print(sorted(list(diff))[0])
else:
    print("None")

