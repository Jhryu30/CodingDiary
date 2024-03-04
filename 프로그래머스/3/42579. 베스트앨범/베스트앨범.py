from collections import defaultdict

def solution(genres, plays):
    answer = []
    N = len(genres)
    playlist = defaultdict(list) # genre : [[i,play], ... ]
    
    for i in range(N):
        genre,play = genres[i],plays[i]
        playlist[genre].append([i,play])
        
    genre_rank = [genre for genre in playlist.keys()]
    genre_rank.sort(key=lambda x:sum([iplay[1] for iplay in playlist[x]]), reverse=True)
    
    for genre in genre_rank:
        play = playlist[genre]
        play.sort(key=lambda x:x[1], reverse=True)
        answer.append(play[0][0])
        if len(play)==1:
            continue
        answer.append(play[1][0])
    
    return answer