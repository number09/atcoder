n = int(input())
li_a = map(int, input().split())

ok_list_a = {1, 3, 5, 7, 9}
ok_list_b = {1, 3, 4, 6, 7, 9}
ok_list = ok_list_a.intersection(ok_list_b)

result = 0
for i in li_a:
    filtered_list = list(filter(lambda x: i >= x, ok_list))
    if len(filtered_list) > 0:
        result += i - max(filtered_list)

print(result)

