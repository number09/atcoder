import datetime

li_input = []

for i in range(3):
    li_input.append(list(map(int, input().split())))

for l in li_input:
    st = datetime.datetime(year=2020, month=1, day=1, hour=l[0], minute=l[1], second=l[2])
    en = datetime.datetime(year=2020, month=1, day=1, hour=l[3], minute=l[4], second=l[5])
    df = en - st

    hour = df.seconds // (60 * 60)
    minute = df.seconds % (60 * 60) // 60
    seconds = df.seconds % (60 * 60) % 60
    print('{0} {1} {2}'.format(hour, minute, seconds))
