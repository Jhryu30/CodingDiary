from collections import deque

def solution(user_id, banned_id):
    answer = 0
    N = len(banned_id)
    
    suspect = [] # [banned_id, [그 때 의심되는 user들의 idx]]
    for banned in banned_id:
        current_suspect =  [user_i for user_i,user in enumerate(user_id) if can_banned(user,banned)]
        suspect.append(current_suspect)
        
    suspect.sort(key=len) # 의심 user가 확실한(=몇 명 없는) 순서대로 정렬

    answer_set = set()
    def add_case(suspect, banned_user):
        if not suspect:
            answer_set.add(tuple(sorted(banned_user)))
            return 
        
        # suspect를 iterate하면서 가능한 경우를 banned_user에 update
        [add_case(suspect[1:], banned_user|{i}) for i in suspect[0] if i not in banned_user]
        
    
    add_case(suspect,set())
    answer = len(answer_set)
    
    return answer



def can_banned(user, banned):
    if len(user)!=len(banned):
        return False
    for u,b in zip(user,banned):
        if u!=b:
            if b!='*':
                return False
    return True
