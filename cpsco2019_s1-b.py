s = input()
print("Yes" if len(set([s.count(w) for w in set(s)])) == 1 else "No")