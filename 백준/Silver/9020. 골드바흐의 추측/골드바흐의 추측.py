def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

TC = int(input())
prime = [2]
for prime_cand in range(3,10000,2):
  if is_prime(prime_cand):
    prime.append(prime_cand)
    

for _ in range(TC):
  n = int(input())
  n1 = n//2
  flag = 1
  while flag:
    n2 = n-n1
    if (n1 in prime) and (n2 in prime):
      print(n1, n2)
      flag = 0
      break
    n1-=1