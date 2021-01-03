a, b = input().split()
print(
    max(
        sum(int(w_a) for w_a in a),
        sum(int(w_b) for w_b in b)
    )
)

