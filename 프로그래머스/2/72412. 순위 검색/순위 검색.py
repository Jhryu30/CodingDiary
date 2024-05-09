from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    
    lang = {'cpp':0, 'java':8, 'python':16, '-':[0,8,16]}
    pos = {'backend':0, 'frontend':4, '-':[0,4]}
    work = {'junior':0, 'senior':2, '-':[0,2]}
    food = {'chicken':0, 'pizza':1, '-':[0,1]}
    scores = defaultdict(list) # lpwf
    
    for applicant in info:
        l,p,w,f,s = applicant.split(" ")
        idx = lang[l] | pos[p] | work[w] | food[f]
        scores[idx].append(int(s))
        
    for idx in scores:
        scores[idx].sort()

    lang = {'cpp':[0], 'java':[8], 'python':[16], '-':[0,8,16]}
    pos = {'backend':[0], 'frontend':[4], '-':[0,4]}
    work = {'junior':[0], 'senior':[2], '-':[0,2]}
    food = {'chicken':[0], 'pizza':[1], '-':[0,1]}
        
    for q in query:
        lq,pq,wq,fsq = q.split(" and ")
        fq,sq = fsq.split(" ")
        
        idxs = [i1|i2|i3|i4 for i1 in lang[lq] for i2 in pos[pq] for i3 in work[wq] for i4 in food[fq]]
                     
        ans = 0
        for idx in idxs:
            if scores[idx]:
                score = scores[idx]
                ans += len(score) - bisect.bisect_left(score,int(sq))
                
        answer.append(ans)
    

    return answer