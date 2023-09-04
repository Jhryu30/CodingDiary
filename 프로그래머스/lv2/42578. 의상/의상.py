from collections import defaultdict

def solution(clothes):
    answer = 1
    
    clothes_dict = defaultdict(int)
    for name,type in clothes:
        clothes_dict[type] += 1
        
    for type in clothes_dict.keys():
        answer = answer*(clothes_dict[type]+1)
        
    return answer - 1