import sys
sys.setrecursionlimit(10**6)

S = list(map(int, list(sys.stdin.readline().rstrip())))

visited_ones = [False for _ in range(len(S))]
visited_zeros = [False for _ in range(len(S))]

def dfs(S, v, visited, sr):
	visited[v] = True
	new_v = v+1
	if new_v >= len(S):
		return False
	if S[new_v]==sr and not visited[new_v]:
		dfs(S, new_v, visited, sr)
		return True
	else:
		return False

ones_ = 0; zeros_ = 0
for s_idx in range(len(S)):
	if S[s_idx]==0 and not visited_ones[s_idx]:
		dfs(S, s_idx, visited_ones, sr=0)
		ones_ += 1
	if S[s_idx]==1 and not visited_zeros[s_idx]:
		dfs(S, s_idx, visited_zeros, sr=1)
		zeros_ += 1
		
print(min(ones_, zeros_))