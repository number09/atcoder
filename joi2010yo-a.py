i_total = int(input())
li_book = []
for i in range(9):
    li_book.append(int(input()))
print(i_total - sum(li_book))