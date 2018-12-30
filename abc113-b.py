n = int(input())
t, a = map(int, input().split())
li_h = list(map(int, input().split()))

li_kion = [{'index': idx + 1, 'abs': abs(a - (t - (h * 0.006)))} for idx, h in enumerate(li_h)]

print(sorted(li_kion, key=lambda x: x['abs'])[0]['index'])


