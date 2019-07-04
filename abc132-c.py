n = int(input())

li_q = list(map(int, input().split()))

abc, arc = sorted(li_q)[:n // 2], sorted(li_q)[n // 2:]

print(arc[0] - abc[-1])