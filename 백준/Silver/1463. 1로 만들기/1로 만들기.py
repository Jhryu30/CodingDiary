from collections import deque

N = int(input())
visited = [0 for _ in range(N+1)]

def dfs(v, visited):
  queue = deque()
  queue.append(v)
  visited[v] = 1

  while queue:
    v = queue.popleft()
    if v==1:
      return visited[v]-1
    elif v<1:
      continue

    if v%3==0:
      new_v = v//3
      if not visited[new_v]:
        queue.append(new_v)
        visited[new_v] = visited[v]+1

    if v%2==0:
      new_v = v//2
      if not visited[new_v]:
        queue.append(new_v)
        visited[new_v] = visited[v]+1

    new_v = v-1
    if not visited[new_v]:
      queue.append(new_v)
      visited[new_v] = visited[v]+1

print(dfs(N, visited))