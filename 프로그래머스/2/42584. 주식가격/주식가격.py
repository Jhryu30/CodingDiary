def solution(prices):
    N = len(prices)
    answer = [0 for _ in range(N)]
    
    stack = []
    for i,v in enumerate(prices):
        while stack and prices[stack[-1]]>v:
            day = stack.pop()
            answer[day] = i-day
        stack.append(i)
    
    while stack:
        day = stack.pop()
        answer[day] = N-day-1
    return answer