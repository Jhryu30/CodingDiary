fib = [0 for _ in range(91)]
fib[0]=0
fib[1]=1

N = int(input())
i=0
while i<=N-2:
  fib[i+2] = fib[i]+fib[i+1]
  i+=1
print(fib[N])