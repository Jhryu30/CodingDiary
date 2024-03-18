from itertools import permutations

def solution(numbers):
    answer = 0
    
    candidates = []
    for i in range(1,len(numbers)+1):
        candidates += [int(''.join(x)) for x in permutations(numbers,i)]
    candidates = list(set(candidates))
    
    def is_prime(num):
        for i in range(2,int(num**0.5)+1):
            if not num%i:
                return False
        return True
    
    for cand in candidates:
        if cand==0 or cand==1:
            continue
        if is_prime(cand):
            answer += 1
            
    return answer