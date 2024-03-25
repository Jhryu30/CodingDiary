# (BOJ) 벽 부수고 이동하기

from collections import deque

N,M = map(int, input().split(' '))
graph = [list(map(int,list(input()))) for _ in range(N)]

visited = [[[0,0] for _ in range(M)] for _ in range(N)]

def bfs(graph,v,visited):
  queue = deque()
  queue.append(v)
  visited[0][0][0] = 1
  if len(graph)==1 and len(graph[0])==1:
    return 1

  while queue:
    x,y,crash = queue.popleft()
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      new_x,new_y = x+dx,y+dy
      if new_x<0 or new_y<0 or new_x>=N or new_y>=M:
        continue
      elif new_x==N-1 and new_y==M-1:
        return visited[x][y][crash]+1
      elif not graph[new_x][new_y] and not visited[new_x][new_y][crash]:
        visited[new_x][new_y][crash] = visited[x][y][crash]+1
        queue.append((new_x,new_y,crash))
      elif graph[new_x][new_y] and not crash:
        visited[new_x][new_y][1] = visited[x][y][0]+1
        queue.append((new_x,new_y,1))
  return -1

answer = bfs(graph,(0,0,0),visited)
print(answer)