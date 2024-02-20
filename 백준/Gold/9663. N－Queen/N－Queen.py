N = int(input())
cnt = 0

R = [0 for _ in range(N)] # 각 행에서 몇번째 column에 퀸을 놓을지 저장

def n_queen(row,R):
  global cnt
  if row==N:
    cnt += 1
    return

  for col in range(N):
    R[row]=col

    flag = True
    for prev_row in range(row):
      if R[prev_row]==R[row] or abs(R[prev_row]-R[row])==abs(prev_row-row):
        flag = False
        break
    if flag:
      n_queen(row+1,R)
      R[row]=0

n_queen(0,R)
print(cnt)