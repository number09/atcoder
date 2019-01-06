s = input()
t = int(input())

words = {w: s.count(w) for w in ('U', 'D', 'L', 'R', '?')}

abs_udlr = abs(words["U"] - words["D"]) + abs(words["L"] - words["R"])

if t == 1:
    print(abs_udlr + words["?"])

else:
    if abs_udlr >= words["?"]:
        print(abs_udlr - words["?"])
    else:
        if (words["?"] - abs_udlr) % 2 == 0:
            print("0")
        else:
            print("1")




