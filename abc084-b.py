import re

int_a, int_b = map(int, input().split())
int_s = input()

pattern = '\d{' + str(int_a) + '}-\d{' + str(int_b) + '}$'

r = re.compile(pattern)

if r.match(int_s):
    print("Yes")
else:
    print("No")





