s = input()

w_l = s.split('S')
print(max([m for m in map(len, w_l)]))