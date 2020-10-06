li_w = []
li_k = []
for i in range(10):
    li_w.append(int(input()))
for i in range(10):
    li_k.append(int(input()))
print(
    sum(sorted(li_w, reverse=True)[:3]),
    sum(sorted(li_k, reverse=True)[:3])
)

