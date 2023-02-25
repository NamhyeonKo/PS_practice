md = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ['MON','TUE','WED','THU','FRI','SAT','SUN']

m, d = map(int,input().split())
day = 0

for i in range(m-1):
    day += md[i]

day += d
print(week[day % 7 - 1])