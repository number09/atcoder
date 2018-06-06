int_n = int(input())
blue_card_ar = [input() for i in range(int_n)]

int_m = int(input())
red_card_ar = [input() for i in range(int_m)]

result_ar = []
for x in blue_card_ar:
    result_ar.append(blue_card_ar.count(x) - red_card_ar.count(x))

print(max(result_ar) if max(result_ar) > 0 else 0)


