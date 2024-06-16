from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    graph = defaultdict(list)
    profit = defaultdict(int)
    
    for child,parent in zip(enroll,referral):
        graph[child].append(parent)
        
    for person,price in zip(seller,amount):
        price*=100
        while not person=='-' and price>0:
            rest = int(0.1*price)
            profit[person] += price-rest
            person, price = graph[person][0], rest
        if person=='-':
            profit[person]+=price
    
    for person in enroll:
        answer.append(profit[person])
        
    return answer