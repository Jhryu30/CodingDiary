N,B = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

def my_mult(matrix1,matrix2):
  m1 = matrix1
  m2 = [[matrix2[i][j] for i in range(N)] for j in range(N)]
  new_matrix = [[0 for _ in range(N)] for _ in range(N)]
  for i in range(N):
    for j in range(N):
      row = m1[i]; col = m2[j]
      mul = sum([row[ij]*col[ij] for ij in range(N)])%1000
      new_matrix[i][j] = mul%1000
  return new_matrix

def squareNleft(m,B):
  Q=B//2; R=B%2
  if Q>1:
    m1 = squareNleft(m,Q)
    m2 = my_mult(m1,m1)
    m = my_mult(m2,m) if R else m2
    return m
  else:
    m2 = my_mult(m,m)
    m = my_mult(m2,m) if R else m2
    return m

if B>1:
  answer = squareNleft(matrix,B)
else:
  matrix2 = [[0 for _ in range(N)] for _ in range(N)]
  for i in range(N):
    matrix2[i][i]=1
  answer = my_mult(matrix,matrix2)
for i in range(N):
  print(*answer[i])