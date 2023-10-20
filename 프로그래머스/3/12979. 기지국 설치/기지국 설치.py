def solution(n, stations, w):
    answer = 0
    cover = 2*w+1
    
    s_prev = stations[0]
    if s_prev-w>1:
        no_wifi = s_prev-w-1
        answer += no_wifi//cover + int(no_wifi%cover > 0)
    for s_new in stations[1:]:
        if s_new-s_prev>2*w:
            no_wifi = s_new-s_prev-cover
            answer += no_wifi//cover + int(no_wifi%cover > 0)
        s_prev = s_new
    if s_prev+w<n:
        no_wifi = n-s_prev-w
        answer += no_wifi//cover + int(no_wifi%cover > 0)
        
    return answer