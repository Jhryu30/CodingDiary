N,M = map(int, input().split())
blocks = [list(map(int,input().split())) for _ in range(N)]

s1 = N*M

s2 = sum(blocks[0])
for n in range(1,N):
  s2 += sum([abs(blocks[n-1][m] - blocks[n][m]) for m in range(M)])
s2 += sum(blocks[-1])

s3 = sum([blocks[n][0] for n in range(N)])
for m in range(1,M):
  s3 += sum([abs(blocks[n][m-1] - blocks[n][m]) for n in range(N)])
s3 += sum([blocks[n][-1] for n in range(N)])

result = 2*s1+s2+s3
print(result)