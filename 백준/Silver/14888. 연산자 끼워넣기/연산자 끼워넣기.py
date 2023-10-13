from itertools import permutations
# N : 수의 개수
# A1, A2
# +,-,*,/ 

# output : max, min

# 14888
N = int(input())
numbers = list(map(int, input().split()))
eqn_lst = list(map(int, input().split())) # plus, minus, multiplication, division
result_lst = []

def calculate(eqn_lst, result, idx):
  global numbers, result_lst

  if idx==N:
    result_lst.append(result)
    return
  
  for i in range(4):
    if eqn_lst[i]>0:
      eqn_lst[i] -= 1
      if i==0:
        result_new = result + numbers[idx]
        calculate(eqn_lst, result_new, idx=idx+1)
      elif i==1:
        result_new = result - numbers[idx]
        calculate(eqn_lst, result_new, idx+1)
      elif i==2:
        result_new = result * numbers[idx]
        calculate(eqn_lst, result_new, idx+1)
      else:
        if result>=0:
          result_new = result // numbers[idx]
        else:
          result_new =  -((-1*result) // numbers[idx])
        calculate(eqn_lst, result_new, idx+1)
      eqn_lst[i] += 1

calculate(eqn_lst, numbers[0],1)
print(max(result_lst))
print(min(result_lst))