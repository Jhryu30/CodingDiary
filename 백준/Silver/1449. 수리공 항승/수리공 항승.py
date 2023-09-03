import sys

N, L = map(int, sys.stdin.readline().split())
pipe = sorted(list(map(int, sys.stdin.readline().split())))

cnt = 1
tape = pipe[0]
for i in pipe:
  if i <= tape+L-1:
    continue
  else:
    tape = i
    cnt+=1
print(cnt)