def dfs(graph, v, visited):
  visited[v] = True
  new_v = graph[v]-1 # idx
  if not visited[new_v]:
    dfs(graph, new_v, visited)


T = int(input())
for _ in range(T):
  N = int(input())
  graph = list(map(int, input().split())) # input_node(v):idx-1 -> output_node(new_v):lst[idx]
  visited = [False for _ in range(N+1)]
  cnt = 0
  for node in range(N):
    if not visited[node]:
      dfs(graph, node, visited)
      cnt += 1
  print(cnt)