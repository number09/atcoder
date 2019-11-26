n = int(input())
s = input()

w_n = n % 26

print("".join([chr(65 + (ord(w) - 65 + w_n) % 26) for w in s]))

