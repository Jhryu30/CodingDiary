def solution(brown, yellow):
    answer = []
    # yellow : w*h -> brown+yellow : (w+2)*(h+2)
    total = brown+yellow
    for w in range(1,yellow+1):
        if yellow%w:
            continue
        h = yellow//w
        if (w+2)*(h+2)==total:
            return [h+2,w+2]
        