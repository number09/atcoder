h, w = map(int, input().split())

answer = list()

for i in range(h):
    r = list(input().split())
    if "snuke" in r:
        answer = [chr(r.index("snuke") + 65), str(i + 1)]
print("".join(answer))


