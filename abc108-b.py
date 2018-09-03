int_x1, int_y1, int_x2, int_y2 = map(int, input().split())

int_x3 = int_y3 = int_x4 = int_y4 = 0

int_x = int_x2 - int_x1
int_y = int_y2 - int_y1

print(int_x2 - int_y, int_y2 + int_x, int_x1 - int_y, int_y1 + int_x)

