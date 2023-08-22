import sys
sys.setrecursionlimit(10**5)

N = int(input())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


def dfs(graph, v, visited):
  x,y = v
  if x<=-1 or x>=N or y<=-1 or y>=N:
    return False
  if graph[x][y]==1 and not visited[x][y]:
    visited[x][y] = 1
    for dx,dy in [[-1,0], [1,0], [0,-1], [0,1]]:
      dfs(graph, [x+dx, y+dy], visited)
    return True
  return False

result = []
old_num = 0
for i in range(N):
  for j in range(N):
    if dfs(graph, [i,j], visited):
      new_num = sum([sum(row) for row in visited])
      result.append(new_num-old_num)
      old_num = new_num
print(len(result))
for num in sorted(result):
  print(num)