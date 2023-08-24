from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(graph, v, visited):
  x,y = v
  queue = deque()
  queue.append((x,y))
  visited[x][y] = 1

  while queue:
    x,y = queue.popleft()
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
      new_x = x+dx; new_y = y+dy
      if new_x==N and new_y==M:
        return visited[x][y]+1
      if new_x<=-1 or new_x>=N or new_y<=-1 or new_y>=M:
        continue
      if graph[new_x][new_y]==1 and not visited[new_x][new_y]:
        visited[new_x][new_y] = visited[x][y]+1
        queue.append((new_x,new_y))

bfs(graph, [0,0], visited)
print(visited[N-1][M-1])