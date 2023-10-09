from collections import deque
import sys
input = sys.stdin.readline

M,N,H = map(int,input().split())

queue = deque()
graph = []
for h in range(H):
	graph_h = []
	for n in range(N):
		graph_hn = list(map(int, input().split()))
		graph_h.append(graph_hn)
		for m in range(M):
			if graph_hn[m]==1:
				queue.append([m,n,h])
	graph.append(graph_h)
    
day=0
while queue:
  v = queue.popleft()
  x,y,z = v
  for dx,dy,dz in [(-1, 0, 0),(1, 0, 0),(0, -1, 0),(0, 1, 0),(0, 0, -1),(0, 0, 1)]:
    new_x=x+dx; new_y=y+dy; new_z=z+dz
    new_v = [new_x,new_y,new_z]
    if new_x<=-1 or new_y<=-1 or new_z<=-1 or new_x>=M or new_y>=N or new_z>=H:
      continue
    elif graph[new_z][new_y][new_x]==-1:
      continue
    else:
      if not graph[new_z][new_y][new_x]:
        graph[new_z][new_y][new_x] = graph[z][y][x]+1
        queue.append(new_v)
        day = max(day,graph[new_z][new_y][new_x]-1)

for h in range(H):
    for n in range(N):
        if 0 in graph[h][n]:
            print(-1)
            exit()
        if h == H-1 and n == N-1:
            print(day)