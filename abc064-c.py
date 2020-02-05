int_n = int(input())
arr_int_a = list(map(int, input().split()))

w_s = set()
counter = 0
for i in arr_int_a:
    if i < 3200:
        w_s.add(i // 400)
    else:
        counter += 1

print(len(w_s) if len(w_s) != 0 else 1, len(w_s) + counter)



