int_n = int(input())

result = False
plan_array = [[0, 0, 0]]

for n in range(int_n):
    plan_array.append(list(map(int, input().split())))


print(plan_array)

for n in range(int_n):
    dt = plan_array[n+1][0] - plan_array[n][0]
    dist = plan_array[n+1][1] - plan_array[n][1] + \
        plan_array[n+1][2] - plan_array[n][2]

    if dist > dt:
        result = False
        break

    if dt & 1 and dist & 1:
        result = True
    else:
        result = False

if result:
    print('YES')
else:
    print('No')

