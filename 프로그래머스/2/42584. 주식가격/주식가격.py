def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # # method.1
    # for i,p_i in enumerate(prices[:-1]):
    #     for j,p_j in enumerate(prices[i+1:]):
    #         if p_i>p_j:
    #             answer[i]=j+1
    #             break
                
    # method.2
    previous = []
    for i,p_i in enumerate(prices):
        while previous and p_i<previous[-1][1]:
            j = previous.pop()[0]
            answer[j]=i-j
        previous.append([i,p_i])
    
    return answer