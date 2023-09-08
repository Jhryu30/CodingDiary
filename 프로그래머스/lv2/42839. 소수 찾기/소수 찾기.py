from itertools import permutations

def solution(numbers):
    answer = 0
    
    permuted = []
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            permuted.append(int(''.join(s for s in p)))
    permuted = list(set(permuted))
    
    for p in permuted:
        if check_prime(p):
            answer += 1
    
    return answer

def check_prime(x):
    if x==0 or x==1:
        return False
    if x==2 or x==3:
        return True
    
    for i in range(2,x//2+1):
        if x%i == 0:
            return False
    return True