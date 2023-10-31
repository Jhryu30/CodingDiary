N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dir_dict = {1:[0,-1], 2:[-1,-1], 3:[-1,0], 4:[-1,1], 5:[0,1], 6:[1,1], 7:[1,0], 8:[1,-1]}
cloud = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]] # initial

for _ in range(M):
  d,s = map(int, input().split())

  dx,dy = dir_dict[d]
  dx*=s; dy*=s

  cloud_new = []
  visited = [[0 for _ in range(N)] for _ in range(N)]
  for c_x,c_y in cloud:
    new_x = c_x+dx; new_y=c_y+dy
    if new_x<0 or new_x>=N: new_x %= N
    if new_y<0 or new_y>=N: new_y %= N
    cloud_new.append([new_x,new_y])
    visited[new_x][new_y] = 1

    A[new_x][new_y] += 1 # step2

  for x,y in cloud_new:
    # step4
    count = 0
    for diag_dir in [2,4,6,8]:
      diag_x,diag_y = dir_dict[diag_dir]
      new_x = x+diag_x; new_y = y+diag_y
      if new_x<0 or new_y<0 or new_x>=N or new_y>=N:
        continue
      else:
        count += int(A[new_x][new_y]>0)

    A[x][y] += count

  cloud = []
  for x in range(N):
    for y in range(N):
      if A[x][y]>=2 and not visited[x][y]:
        cloud.append([x,y])
        A[x][y] -= 2

result = sum([sum(A[row]) for row in range(N)])
print(result)