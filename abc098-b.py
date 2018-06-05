int_n = int(input())
str_s = input()

result_ar = []
for i in range(len(str_s)):
    # print(str_s[:i], str_s[i:])
    result_ar.append(len(set(str_s[:i]) & set(str_s[i:])))

print(max(result_ar))
