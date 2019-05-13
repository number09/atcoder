R, G, B, N = map(int, input().split())

counter = 0
for r in range((N // R) + 1):
    for g in range(((N - (r * R)) // G) + 1):
        w_b_sum = N - ((R * r) + (G * g))

        if w_b_sum % B == 0 and w_b_sum >= 0:
            # print(r, g, (w_b_sum // B))
            counter += 1
print(counter)
