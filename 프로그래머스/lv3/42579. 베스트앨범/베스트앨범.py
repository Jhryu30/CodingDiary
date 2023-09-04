from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # (1)album_freq (2,3)album
    album = defaultdict(list) # {genres:[[#plays:i],[]..]}
    album_freq = defaultdict(int)
    for i in range(len(genres)):
        album[genres[i]].append([plays[i],i])
        album_freq[genres[i]] += plays[i]
    
    # sort with album_freq (cond.1) : freq=[[genres,sum(plays)],...]
    freq = sorted([[k,v] for k,v in album_freq.items()], key=lambda x:x[1], reverse=True) 
    
    for f in freq:
        genres = f[0]
        # sort with #plays(cond.2)->i(cond.3)
        album[genres].sort(key=lambda x:(-x[0],x[1]))
        
        if len(album[genres])==1:
            answer.append(album[genres][0][1])
        else:
            answer.append(album[genres][0][1])
            answer.append(album[genres][1][1])
    
    return answer