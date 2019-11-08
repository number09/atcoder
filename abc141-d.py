import heapq
import math

n, m = map(int, input().split())
li_a = list(map(lambda x: x * -1, (map(int, input().split()))))
heapq.heapify(li_a)


for i in range(m):
    w = heapq.heappop(li_a)
    heapq.heappush(li_a, math.ceil(w / 2))

print(sum(li_a) * -1)
