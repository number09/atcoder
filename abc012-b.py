import datetime
n = int(input())
t = tuple(map(int, str(datetime.timedelta(seconds=n)).split(":")))
print("{:02}:{:02}:{:02}".format(*t))

