from collections import deque

T = int(input())
gear = [deque(map(int,list(input()))) for _ in range(T)]; gear_old = [[g[i] for i in range(8)] for g in gear]
K = int(input())
k_order = [list(map(int, input().split())) for _ in range(K)]

l,r = -2,2
for t,k in k_order:
  t-=1
  gear[t].rotate(k)  
  kk=k
  for tt in range(t,T-1):
    if gear_old[tt][r]==gear_old[tt+1][l]:
      break
    else:
      kk=-kk
      gear[tt+1].rotate(kk)
  kk=k
  for tt in range(t,0,-1):
    if gear_old[tt][l]==gear_old[tt-1][r]:
      break
    else:
      kk=-kk
      gear[tt-1].rotate(kk)
  gear_old = [[g[i] for i in range(8)] for g in gear]

answer=0
for i in range(T):
  answer += int(gear[i][0]>0)

print(answer)