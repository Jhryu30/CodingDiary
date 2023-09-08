def solution(brown, yellow):
    answer = []
    
    if yellow==1:
        return [3,3]
    
    else:
        for i in range(1,yellow//2+1):
            if yellow%i == 0:
                height = i; width = yellow//i
                if 2*(height+width)+4 == brown:
                    return [width+2, height+2]
