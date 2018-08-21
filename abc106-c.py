str_s = input()
int_k = int(input())

result = ""

for s in str_s[0:int_k]:
    if s != "1":
        result = s
        break
else:
    result = "1"

print(result)
