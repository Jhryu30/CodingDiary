from itertools import combinations

def count123(N):
  cnt = 0
  for threes in reversed(range(N//3+1)):
    rest = N - 3*threes
    for twos in reversed(range(rest//2+1)):
      ones = rest - 2*twos
      total_idx3 = list(range(threes+twos+ones))
      total_idx2 = list(range(twos+ones))
      cnt += len(list(combinations(total_idx3, threes))) * len(list(combinations(total_idx2, twos)))
  return cnt

for test_case in range(int(input())):
  N = int(input())
  print(count123(N))