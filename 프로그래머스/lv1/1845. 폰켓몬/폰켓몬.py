from collections import defaultdict

def solution(nums):
    answer = 0
    N = int(len(nums)/2)
    pokemon = defaultdict(int)
    for p in nums:
        pokemon[p]+=1
    
    pokemon_left = len(pokemon.keys())
    if pokemon_left>=N:
        answer += N
    else:
        answer += pokemon_left
        
    return answer