def solution(n, s):
    answer = []
    
    start = s//n
    
    if start==0:
        return [-1]
    
    r = s%n
    if not r:
        answer = [start]*n
    else:
        answer = [start]*(n-r)+[start+1]*r
        
    return answer