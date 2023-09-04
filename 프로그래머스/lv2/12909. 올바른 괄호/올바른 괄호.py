def solution(s):
    answer = True
    
    left = []
    for i in s:
        if i=='(':
            left.append(i)
        else:
            if len(left)>0:
                left.pop()
            else:
                return False
            
    if len(left)>0:
        return False
        
    return True