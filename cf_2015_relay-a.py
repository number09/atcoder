t = int(input())
answer = 0
for l in range(10):
    w_ls = list(range(1, 21)) if l % 2 == 0 else sorted(list(range(1, 21)), reverse=True)
    ls = [n + (20 * l) for n in w_ls]
    answer += ls[t - 1]
print(answer)


