import sys

N = int(sys.stdin.readline())
timetable = []
for _ in range(N):
	i,j = map(int, sys.stdin.readline().split())
	timetable.append([i,j])
	
timetable.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = timetable[0][1]
for i in range(1,N):
	if timetable[i][0]>=end_time:
		cnt += 1
		end_time = timetable[i][1]
print(cnt)