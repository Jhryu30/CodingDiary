import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = list()

for i in range(N):
  x = int(input())
  
  if x:
    heapq.heappush(heap, x)
    
  else:
    if heap:
      print(heapq.heappop(heap))
    else:
      print(0)