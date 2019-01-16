from decimal import Decimal, ROUND_HALF_UP


deg, dis = map(int, input().split())

li_deg = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']


def get_deg(deg):
    for idx, v in enumerate((112.5 + 225.0 * i for i in range(0, 16)), start=1):
        if 0 <= (deg - v) < 225.0:
            return idx if idx != 16 else 0
    else:
        return 0


def get_dis(dis):
    li_from = [0.0,0.3,1.6,3.4,5.5,8,   10.8,13.9,17.2,20.8,24.5,28.5,32.7]
    li_to   = [0.2,1.5,3.3,5.4,7.9,10.7,13.8,17.1,20.7,24.4,28.4,32.6,12000]
    li_f = [i for i in range(13)]

    for fr, to, f in zip(li_from, li_to, li_f):
        d = Decimal(str(dis / 60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        if fr <= float(d) <= to:
            return f


p_dis = get_dis(dis)
p_deg = li_deg[get_deg(deg)]
print('C' if p_dis == 0 else p_deg, p_dis)
