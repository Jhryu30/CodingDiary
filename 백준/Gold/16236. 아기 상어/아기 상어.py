# 16236 아기 상어

from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

def dfs(graph,v,size):
  queue = deque()
  queue.append(v)
  candidate = []
  visited = [[0 for _ in range(N)] for _ in range(N)]

  while queue:
    x,y = queue.popleft()
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      new_x = x+dx; new_y = y+dy
      if new_x<0 or new_y<0 or new_x>=N or new_y>=N:
        continue
      if graph[new_x][new_y]>size:
        continue
      
      if not visited[new_x][new_y]:
        fish = graph[new_x][new_y]
        dist = visited[x][y]+1
        if 0<fish and fish<size:
          candidate.append((new_x,new_y,dist))
        visited[new_x][new_y] = dist
        queue.append((new_x,new_y))
  
  candidate.sort(key=lambda x:(x[2],x[0],x[1]))
  return candidate

# initial values for: v, size, and cnt
answer = 0
for x in range(N):
  if 9 in graph[x]:
    y = graph[x].index(9)
    break
size, cnt = 2,0


while True:
  v = (x,y)
  graph[x][y] = 0
  candidate = dfs(graph,v,size)
  if not candidate:
    break
  new_x,new_y,dist = candidate[0]
  x,y = new_x,new_y
  cnt += 1
  if cnt==size:
    size += 1
    cnt = 0
  answer += dist


print(answer)