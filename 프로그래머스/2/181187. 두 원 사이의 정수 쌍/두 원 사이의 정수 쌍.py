from math import floor, ceil

def solution(r1, r2):
    answer = 0
    
    R,r = r2**2, r1**2
    for x in range(r2):
        min_y = max(1,ceil((max(r-x**2,0))**0.5))
        max_y = floor((R-x**2)**0.5)
        answer += max_y-min_y+1
        
        
    return 4*answer