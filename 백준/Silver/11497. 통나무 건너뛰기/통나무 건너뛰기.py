from collections import deque

T = int(input())

for _ in range(T):
  N = int(input())
  log = deque(sorted(list(map(int, input().split()))))
  i=0
  final = [0 for _ in range(N)]
  while log:
    v = log.popleft()
    final[i] = v
    i = -i if i<0 else -(i+1)
  
  dlog = [0 for _ in range(5)]
  dlog = [abs(l2-l1) for l1,l2 in zip([0]+final, final+[final[0]])][1:]
  print(max(dlog))