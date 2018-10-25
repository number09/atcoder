n = int(input())

town = dict()
for i in range(n):
    name, zinko = input().split()
    town[name] = int(zinko)

goukei = sum(town.values())

for k, v in town.items():
        if v > (goukei // 2):
            print(k)
            break
else:
    print("atcoder")
