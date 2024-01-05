from itertools import combinations

# 0:empty, 1:house, 2:chicken
N, M = map(int, input().split())
citymap = [list(map(int, input().split())) for _ in range(N)]

house = [(i,j) for i in range(N) for j in range(N) if citymap[i][j]==1]
chicken = [(i,j) for i in range(N) for j in range(N) if citymap[i][j]==2]

def distance(house_id, chicken):
  s,t = house_id
  d = [abs(s-ch[0])+abs(t-ch[1]) for ch in chicken]
  return min(d)

result = N*N*len(house)
for ch in combinations(chicken,M):
  s = 0
  for house_id in house:
    s += distance(house_id, ch)
  if s<result:
    result = s

print(result)