def solution(n, m, x, y, r, c, k):
    answer = ''
    
    distance = abs(r - x) + abs(c - y)
    
    if distance > k or not (k-distance)%2==0:
        return 'impossible'
    
    dir_dict = {'d':max(0,r-x), 'u':max(0,x-r), 'l':max(0,y-c), 'r':max(0,c-y)}
    k -= distance
    
    answer += 'd'*dir_dict['d']
    x += dir_dict['d']
    dist = min(k//2, n-x)
    answer += 'd'*dist
    dir_dict['u'] += dist
    k -= 2*dist
        
    answer += 'l'*dir_dict['l']
    y -= dir_dict['l']
    dist = min(k//2, y-1)
    answer += 'l'*dist
    dir_dict['r'] += dist
    k -= 2*dist
    
    answer += 'rl'*(k//2)
    answer += 'r'*dir_dict['r'] + 'u'*dir_dict['u']
    
    return answer

