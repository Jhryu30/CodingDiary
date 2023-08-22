import sys
sys.setrecursionlimit(10**5)
input_fcn = sys.stdin.readline
N = int(input_fcn())
area = [list(map(int, input_fcn().split())) for _ in range(N)]

def dfs(graph, v, visited):
  x,y = v
  if x<=-1 or x>=N or y<=-1 or y>=N:
    return False
  if graph[x][y]==1 and not visited[x][y]:
    visited[x][y]=True
    for dx,dy in [[-1,0], [1,0], [0,-1], [0,1]]:
      dfs(graph, [x+dx, y+dy], visited)
    return True
  else:
    return False

result = []
max_ = [max(row) for row in area]
for height in range(max(max_)):
  graph = [[int(val>height) for val in row] for row in area] # 0:danger 1:safe
  visited = [[False for _ in range(N)] for _ in range(N)]
  result_height = 0
  for x_iter in range(N):
    for y_iter in range(N):
      if dfs(graph, [x_iter, y_iter], visited):
        result_height += 1
  result.append(result_height)
print(max(result))