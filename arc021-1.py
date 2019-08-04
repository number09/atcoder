li_grid = list()

for _ in range(4):
    li_grid.append(list(input().split()))

for tate in range(4):
    for yoko in range(3):
        if li_grid[tate][yoko] == li_grid[tate][yoko + 1]:
            print("CONTINUE")
            exit(0)
for tate in range(3):
    for yoko in range(4):
        if li_grid[tate][yoko] == li_grid[tate + 1][yoko]:
            print("CONTINUE")
            exit(0)
print("GAMEOVER")
