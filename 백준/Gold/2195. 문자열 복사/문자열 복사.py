S = input()
P = input()
visited = [False for _ in range(len(P))]

cnt = 1
for p_idx in range(len(P)):
  if not visited[p_idx]:
    visited[p_idx]
    p_idx_end = p_idx
    while P[p_idx:p_idx_end+1] in S:
      p_idx_end += 1
      if p_idx_end >= len(P):
        break
      visited[p_idx_end]=True
    if p_idx_end >= len(P):
      break
    visited[p_idx_end] = False
    cnt +=1

print(cnt)