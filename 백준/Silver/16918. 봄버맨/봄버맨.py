R,C,N = map(int, input().split())
graph = [list(input()) for _ in range(R)]

bomb_dict = {'.':0, 'O':1, 0:'.', 1:'O'}
bomb_graph = [[bomb_dict[b] for b in graph[row]] for row in range(R)]

if N==1:
  result_graph = [''.join([bomb_dict[g] for g in bomb_graph[row]]) for row in range(R)]
  print('\n'.join(result_graph))

elif N%2==0:
  print('\n'.join([''.join(['O' for _ in range(C)]) for _ in range(R)]))

else:
  time = 0
  while time<N-1:
    time += 2
    graph = [[0 for _ in range(C)] for _ in range(R)] # fill with bomb
    for i in range(R):
      for j in range(C):
        if bomb_graph[i][j]:
          graph[i][j]=1
          for di,dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            new_i=i+di; new_j=j+dj
            if new_i<=-1 or new_j<=-1 or new_i>=R or new_j>=C:
              continue
            else:
              graph[new_i][new_j] = 1
    bomb_graph = [[int(not x) for x in graph[row]] for row in range(R)]


  result_graph = [''.join([bomb_dict[g] for g in bomb_graph[row]]) for row in range(R)]
  print('\n'.join(result_graph))