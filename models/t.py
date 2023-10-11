import datetime

time = datetime.datetime.now()
print(time)
time = time.strftime("%Y-%m-%dT%H:%M:%S.%f")
print(time)
