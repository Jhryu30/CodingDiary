from collections import deque

S = int(input())
visited = [[0 for _ in range(2*S+1)] for _ in range(2*S+1)]

def dfs(v,cb, visited):
  queue = deque()
  queue.append([v,cb])

  while queue:
    v,cb = queue.popleft()
    if v==S:
      return visited[v][cb]
    for new_v,new_cb in [[v,v], [v+cb,cb], [v-1,cb]]:
      if new_cb==0:
        continue
      if new_v<0 or new_cb<0 or new_v>=2*S+1 or new_cb>=2*S+1:
        continue
      elif not visited[new_v][new_cb] or visited[new_v][new_cb]>visited[v][cb]+1:
        visited[new_v][new_cb] = visited[v][cb]+1
        queue.append([new_v,new_cb])


result = dfs(1,0,visited)
print(result)