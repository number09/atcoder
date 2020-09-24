n = int(input())
s = input()

print(''.join(sorted(s, key=lambda w: 0 if w == 'J' else 2 if w == 'O' else 3)))