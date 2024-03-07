def solution(word):
    answer = 0
    history = []
    
    def backtracking(current,depth=0):
        nonlocal history
        if ''.join(current)==word:
            return depth
        
        for letter in 'AEIOU':
            current.append(letter)
            if len(current)<=5:
                history.append(''.join(current.copy()))
                backtracking(current,depth+1)
            current.pop()
                
    backtracking([])
    for i,v in enumerate(history):
        if v==word:
            return i+1