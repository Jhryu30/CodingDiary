from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int, input().split())
v = map(int, input().split()) # r,c,d
dir_dict = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
graph = [list(map(int,input().split())) for _ in range(N)] # 0:청소되지 않은 빈 칸 1: 벽

result = 0 # count the room

def clean_room(graph, v):
  global result, dir_dict
  queue = deque()
  queue.append(v)

  while queue:
    r,c,d = queue.popleft()
    if not graph[r][c]:
      graph[r][c] = 2 # 2:청소된 빈 칸
      result += 1
    
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if 0 in [graph[r+1][c], graph[r-1][c], graph[r][c+1], graph[r][c-1]]:
      new_d = (d+3)%4 # -90'회전()
      dr,dc = dir_dict[new_d]
      new_r=r+dr; new_c=c+dc
      if graph[new_r][new_c]==0:
        queue.append([new_r,new_c, new_d])
      else:
        queue.append([r,c,new_d])

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
      new_d = d # 방향 그대로
      dr,dc = dir_dict[(d+2)%4] # 후진
      new_r=r+dr; new_c=c+dc
      if graph[new_r][new_c]==1:
        return
      else:
        queue.append([new_r,new_c,new_d])

clean_room(graph, v)
print(result)