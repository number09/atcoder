a, b, t = map(int, input().split())

cicle = (t - b) // (b - a) if (t - b) % (b - a) == 0 else ((t - b) // (b - a)) + 1
print(b + (b - a) * cicle)

