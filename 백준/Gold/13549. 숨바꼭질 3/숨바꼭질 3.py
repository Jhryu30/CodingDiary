from collections import deque

N,K = map(int, input().split())
M = max(2*N+1, 2*K+1)

def bfs(v,visited):
  queue = deque()
  queue.append(v)

  while queue:
    v = queue.popleft()
    if v==K:
      return visited[v]

    new_v = 2*v
    while v>0 and new_v<=M:
      if new_v==K:
        return visited[v]
      if (not visited[new_v]) or (visited[new_v] > visited[v]+1):
        visited[new_v] = visited[v]
        queue.append(new_v)
        new_v *= 2
      else:
        break

    for new_v in [v-1,v+1]:
      if new_v<0 or new_v>=M:
        continue
      else:
        if (not visited[new_v]) or (visited[new_v] > visited[v]+1):
          visited[new_v] = visited[v]+1
          queue.append(new_v)
          
visited = [0 for _ in range(M)]
visited[N]=1
result = bfs(N,visited)
print(result-1)