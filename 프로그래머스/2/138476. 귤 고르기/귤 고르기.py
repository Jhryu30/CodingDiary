from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    least = [(k,v) for k,v in cnt.items()]
    least.sort(key=lambda x:x[1], reverse=True)
    
    total = 0
    for size,count in least:
        total += count
        answer += 1
        if total>=k:
            break
            
    return answer