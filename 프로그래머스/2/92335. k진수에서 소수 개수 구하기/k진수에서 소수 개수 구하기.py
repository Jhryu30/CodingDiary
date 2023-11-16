def solution(n, k):
    answer = 0
    k_i=0
    while True:
        if n<k**k_i: break
        k_i+=1
    
    result=''
    for i in range(k_i-1,-1,-1):
        d,n = divmod(n,k**i)
        if d==0:
            if len(result):
                answer += check_prime(int(result))
            result=''
        else:
            result+=str(int(d))
    
    if len(result):
        answer += check_prime(int(result))
        
    return answer

def check_prime(p):
    p = int(p)
    if p==1:
        return 0
    for i in range(2,int(p**(1/2))+1):
        if p%i==0:
            return 0
    return 1
            