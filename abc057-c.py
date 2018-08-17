import math
int_n = int(input())

li_res = list()

for a in range(1, int(math.sqrt(int_n))):
   if int_n % a == 0:
        b = int_n // a
        li_res.append(max([len(str(a)), len(str(b))]))

print(min(li_res))




