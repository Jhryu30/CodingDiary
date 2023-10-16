from collections import deque

def dfs(graph, start_v, visited):
  queue = deque()
  queue.append(start_v)

  while queue:
    h,r,c = queue.popleft()
    for dh,dr,dc in [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]:
      new_h,new_r,new_c = h+dh,r+dr,c+dc
      if new_h<=-1 or new_r<=-1 or new_c<=-1 or new_h>=L or new_r>=R or new_c>=C:
        continue
      elif graph[new_h][new_r][new_c]=='#':
        continue
      elif graph[new_h][new_r][new_c]=='E':
        return visited[h][r][c]+1
      elif graph[new_h][new_r][new_c]=='.' and not visited[new_h][new_r][new_c]:
        visited[new_h][new_r][new_c] = visited[h][r][c]+1
        queue.append([new_h,new_r,new_c])
        
  return False

L,R,C = 1,1,1

while L>0 and R>0 and C>0:
  L,R,C = map(int, input().split())

  graph = []
  for height in range(L):
    graph_height = []
    for row in range(R):
      graph_row = list(input())
      if 'S' in graph_row:
        start = [height,row,graph_row.index('S')]
      graph_height.append(graph_row)
    graph.append(graph_height)
    list(input())

  visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

  result = dfs(graph, start, visited)

  if result:
    print(f'Escaped in {result} minute(s).')
  elif L>0 and R>0 and C>0:
    print('Trapped!')