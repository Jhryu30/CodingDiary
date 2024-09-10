from collections import defaultdict

def solution(scores):
    answer = 0
    wanho = scores[0]
    w = sum(wanho)
    score_dict = defaultdict(list)
    for x,y in scores[1:]:
        if x+y>w:
            score_dict[x].append(y)
        if x>wanho[0] and y>wanho[1]:
            return -1
        
    if not score_dict:
        return 1
    xs = sorted(list(score_dict.keys()),reverse=True)
    max_val = max(score_dict[xs[0]])
    answer = len(score_dict[xs[0]])
    if xs[1:]:
        for x in xs[1:]:
            ys = score_dict[x]
            answer += sum([y>=max_val for y in ys])
            max_val = max(ys+[max_val])
            
    answer += 1
    
    return answer