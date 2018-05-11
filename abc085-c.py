import sys
int_n, int_y = list(map(int, input().split()))

find = False

for ichimanen in range(int_n + 1):
    for gosenen in range(int_n + 1):
        if int_n - ichimanen - gosenen >= 0:
            if ichimanen + gosenen + (int_n - ichimanen - gosenen) == int_n and find is False:
                if (ichimanen * 10000 + gosenen * 5000 + (int_n - ichimanen - gosenen) * 1000) == int_y:
                    find = True
                    print(ichimanen, gosenen, (int_n - ichimanen - gosenen))
                    sys.exit()

if find is False:
    print(-1, -1, -1)




