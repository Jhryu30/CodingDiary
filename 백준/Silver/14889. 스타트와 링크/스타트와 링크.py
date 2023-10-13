import sys
input = sys.stdin.readline

N = int(input()); N2 = N//2
S = [list(map(int, input().split())) for _ in range(N)]

final_result=int(1e9)

def team_split(team1,depth,idx):
  global final_result

  if depth == N2:
    result = 0
    team2 = []
    for i in range(N):
      for j in range(i+1,N):
        if i in team1 and j in team1:
          if i not in team1 or j not in team2:
            result += S[i][j]+S[j][i]
        elif (i not in team1) and (j not in team1):
          result -= S[i][j]+S[j][i]
          team2.append(i); team2.append(j)
          
    if abs(result) < final_result:
      final_result = abs(result)
    return

  for i in range(idx,N):
    if i not in team1:
      team1.append(i)
      team_split(team1,depth+1,i+1)
      team1.pop()

result = team_split([],0,0)
print(final_result)