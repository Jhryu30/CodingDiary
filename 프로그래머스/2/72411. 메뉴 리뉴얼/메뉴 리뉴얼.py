from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for n_course in course:
        candidate_menu = []
        for menus in orders:
            for new_cand in combinations(menus,n_course):
                candidate_menu.append(''.join(sorted(new_cand)))
        candidate = Counter(candidate_menu).most_common()
        if len(candidate):
            max_freq = candidate[0][1]
            answer += [menu for menu,cnt in candidate if cnt>1 and cnt==max_freq]
    answer.sort()
    return answer