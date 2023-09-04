node_num = int(input())
edge_num = int(input())

graph = [[] for _ in range(node_num+1)]
for _ in range(edge_num):
  i, j = map(int,input().split())
  graph[i].append(j)
  graph[j].append(i)

visited = [False for _ in range(node_num+1)]

def dfs(graph, v, visited):
  visited[v]=True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, 1, visited)

print(sum(visited)-1)