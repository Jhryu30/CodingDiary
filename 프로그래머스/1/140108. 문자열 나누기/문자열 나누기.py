from collections import deque

def solution(s):
    answer = 0
    
    equal = 1; unequal = 0
    
    ss = deque(s)
    q = deque() # 첫번째 문자 저장
    
    x = ss.popleft()
    q.append(x)
    # x = q.append(a) # 업데이트 안 되고 있음
    # print(q)
    while q and ss:
        letter = ss.popleft()
        if x == letter:
            equal += 1
        else:
            unequal += 1
        
        if equal == unequal:
            print(q)
            answer += 1
            q.popleft()
            
            if len(ss) != 0:
                x = ss.popleft()
                q.append(x)
                # q.append(ss.popleft())
            equal = 1
            unequal = 0
            
    if len(ss) < 1 and len(q) >= 1: # abracadabr"aa" 
        answer += 1

    return answer