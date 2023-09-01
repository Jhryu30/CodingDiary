N = int(input())
A = list(map(int, input().split()))

subseq_len = [1 for _ in range(N)]

for i in range(len(A)):
  for j in range(i):
    if A[j] > A[i]:
      subseq_len[i] = max(subseq_len[i], subseq_len[j]+1)

print(max(subseq_len))