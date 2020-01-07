s = input()

mibun = s[2]

if mibun == "B":
    print("Bachelor " + s[:2])
elif mibun == "M":
    print("Master " + s[:2])
else:
    print("Doctor " + s[:2])


