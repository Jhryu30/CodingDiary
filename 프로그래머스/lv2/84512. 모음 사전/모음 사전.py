from itertools import permutations

def solution(word):
    answer = 0
    # https://hzoo.tistory.com/12
    vowel_dict = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    digit_ = [781, 156, 31, 6, 1]
    
    for i in range(len(word)):
        answer += digit_[i] * vowel_dict[word[i]]
        
    return answer+len(word)