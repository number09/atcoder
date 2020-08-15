from datetime import datetime

ma, da = map(int, input().split())
mb, db = map(int, input().split())

fdate = datetime.strptime('/'.join(['2012', str(ma), str(da)]), '%Y/%m/%d')
tdate = datetime.strptime('/'.join(['2012', str(mb), str(db)]), '%Y/%m/%d')

print((tdate - fdate).days)