def solution(s):
    answer = 1
    
    if s==s[::-1]:
        return len(s)
    
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            current = s[i:j]
            if current == current[::-1]:
                answer = max(answer, len(current))
                
    return answer