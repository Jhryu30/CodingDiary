def solution(numbers):
    answer = ''
    
    # 질문하기..
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    answer = str(int(''.join(numbers)))
    
    return answer