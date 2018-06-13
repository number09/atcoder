int_n = int(input())

arare_array = input().split()

if len(set(arare_array)) == 4:
    print("Four")
else:
    print("Three")
