H, W, N, M = map(int, input().split())
print((H//(N+1)+int(H%(N+1)>0)) * (W//(M+1)+int(W%(M+1)>0)))