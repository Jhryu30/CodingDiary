from collections import defaultdict
T = int(input())

for _ in range(T):
  N = int(input())
  raw_rank = list(map(int, input().split()))

  team_cnt = defaultdict(int)
  for t in raw_rank:
    team_cnt[t] += 1

  candidate = []
  for t in team_cnt:
    if team_cnt[t]==6:
      candidate.append(t)

  rank = [r for r in raw_rank if r in candidate]
  team = defaultdict(lambda : [0,0,0]) # [cnt,sum,5th]

  for i,t in enumerate(rank):
    team[t][0] += 1
    if team[t][0]<=4:
      team[t][1]+=i+1
    if team[t][0]==5:
      team[t][2] = i+1


  result = min(team.keys(), key=lambda x:(team[x][1],team[x][2]))
  print(result)