N,M = map(int, input().split())
result_lst = []

def backtracking(result):
  global result_lst

  if len(result)==M:
    result_lst.append(' '.join(list(map(str,result))))
    return

  for i in range(1,N+1):
    result.append(i)
    backtracking(result)
    result.pop()

backtracking([])
result_lst.sort()
print('\n'.join(result_lst))