
from datetime import datetime, timedelta, timezone

n = datetime.now()
print (n)
print (str(n))

s = n.timestamp()
print (s)

ms = str(n).split('.')[0]
print (ms)
print (datetime.strptime('2023-12-22 19:23:21', '%Y-%m-%d %H:%M:%S'))

print (datetime.fromtimestamp(1506408808))
print (datetime.utcfromtimestamp(1506408808.591092))

print (datetime(2313,3,3))

print (timezone(timedelta(hours=9)))

print (timedelta(hours=8))