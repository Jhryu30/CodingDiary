from collections import deque

def RGB(x):
  if x=='R':
    return 1
  elif x=='G':
    return 2
  else:
    return 0

N = int(input())
graphO = [list(map(RGB,input())) for _ in range(N)] # R1 G2 B0
graphX = [[int(x>0) for x in graphO[row]] for row in range(N)]

visitedO = [[0 for _ in range(N)] for _ in range(N)]
visitedX = [[0 for _ in range(N)] for _ in range(N)]

def dfs(graph, v, visited, target):
  queue = deque()
  queue.append(v)

  while queue:
    x,y = queue.popleft()
    for dx,dy in [[-1,0],[0,-1],[1,0],[0,1]]:
      new_x=x+dx; new_y=y+dy
      if new_x<0 or new_y<0 or new_x>=N or new_y>=N:
        continue
      elif graph[new_x][new_y]==target and not visited[new_x][new_y]:
        visited[new_x][new_y]=1
        queue.append([new_x,new_y])

cntO=0
for x in range(N):
  for y in range(N):
    if not visitedO[x][y]:
      target = graphO[x][y]
      dfs(graphO,[x,y] ,visitedO, target)
      cntO += 1
cntX=0
for x in range(N):
  for y in range(N):
    if not visitedX[x][y]:
      target = graphX[x][y]
      dfs(graphX,[x,y] ,visitedX, target)
      cntX += 1

print(cntO,cntX)