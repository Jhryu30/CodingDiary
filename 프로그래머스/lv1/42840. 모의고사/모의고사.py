def solution(answers):
    answer = []
    q_num = len(answers)
    s1 = [1,2,3,4,5]*(q_num//5+1)
    s2 = [2,1,2,3,2,4,2,5]*(q_num//8+1)
    s3 = [3,3,1,1,2,2,4,4,5,5]*(q_num//10+1)
    
    a = [0,0,0]
    for i in range(q_num):
        ans = answers[i]
        if s1[i]==ans:
            a[0] += 1
        if s2[i]==ans:
            a[1] += 1
        if s3[i]==ans:
            a[2] += 1
            
    M = max(a)
    answer = [index+1 for index,val in enumerate(a) if val==M]
    return answer