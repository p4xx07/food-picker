import datetime

now = datetime.datetime.now()

mid_day = datetime.datetime(now.year, now.month, now.day, 12, 30)
print(str(mid_day))

diff = now - mid_day

print(str(diff))