timeStr = input()
timeSplit = timeStr.split(' ')
hour = int(timeSplit[0])
minute = int(timeSplit[1])

res_hour = hour
res_minute = minute-45

if res_minute < 0:
    res_minute = res_minute + 60
    res_hour = res_hour - 1

if res_hour < 0:
    res_hour = res_hour + 24

print(str(res_hour) + ' ' + str(res_minute))