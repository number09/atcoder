n = int(input())
cards_t = []

for _ in range(n):
    cards_t.append(int(input()))

cards_t.sort()
cards_h = sorted(list(set(range(1, (2 * n) + 1)).difference(set(cards_t))))

fields = []
counter = 0
while len(cards_t) !=0 and len(cards_h) != 0:

    wk_cards = cards_t if counter % 2 == 0 else cards_h
    if len(fields) == 0:
        w = wk_cards[0]
        fields.append(w)
        wk_cards = wk_cards[1:]

    else:
        latest = fields[-1]
        for idx, x in enumerate(wk_cards):
            if latest < x:
                fields.append(x)
                wk_cards.remove(x)
                break
        else:
            fields = []

    if counter % 2 == 0:
        cards_t = wk_cards
    else:
        cards_h = wk_cards
    counter += 1
print(len(cards_h))
print(len(cards_t))





