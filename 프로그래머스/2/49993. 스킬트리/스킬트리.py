from collections import deque

def solution(skill, skill_trees):
    answer = 0
    skill_dict = {s:i for i,s in enumerate(skill)}
    
    
    for skill_tree in skill_trees:
        flag = 1
        prev = -1
        for s in skill_tree:
            if s in skill_dict:
                if skill_dict[s]==prev+1:
                    prev = skill_dict[s]
                else:
                    flag = 0
                    break
                    
        if flag: answer += 1
        
    return answer