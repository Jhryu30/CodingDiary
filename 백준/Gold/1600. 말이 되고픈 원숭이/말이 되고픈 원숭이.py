from collections import deque

k = int(input())
W,H = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(H)] # 1:obstacle

# k=1
# W,H = 4,4
# world = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]

visited = [[[0 for _ in range(k+1)] for _ in range(W)] for _ in range(H)]

def bfs(graph, v, visited,k):
  x,y = v
  queue = deque()
  queue.append((x,y,0))
  visited[0][0][0] = 1

  while queue:
    x,y,z = queue.popleft()
    if x==H-1 and y==W-1:
      return visited[x][y][z]-1

    for move in ['horse', 'monkey']:
      if move=='horse':
        if z>=k:
          continue
        for dx,dy in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
          new_x = x+dx; new_y = y+dy

          if new_x<0 or new_y<0 or new_x>=H or new_y>=W:
            continue
          if not visited[new_x][new_y][z+1] and not world[new_x][new_y]:
            visited[new_x][new_y][z+1] = visited[x][y][z]+1
            queue.append((new_x,new_y,z+1))


      else: # 'monkey'
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
          new_x = x+dx; new_y = y+dy
          if new_x<0 or new_y<0 or new_x>=H or new_y>=W:
            continue
          if not visited[new_x][new_y][z] and not world[new_x][new_y]:
            visited[new_x][new_y][z] = visited[x][y][z]+1
            queue.append((new_x,new_y,z))

  return -1

result = bfs(world, (0,0), visited,k)
print(result)