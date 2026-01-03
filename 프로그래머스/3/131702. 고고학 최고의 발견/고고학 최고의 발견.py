from itertools import product
from copy import deepcopy

def solution(clockHands):
    N = len(clockHands)
    answer = 16**N

    def rotate(block, loc, num):
        i,j = loc
        for ii,jj in [(i-1,j), (i,j-1), (i,j), (i,j+1), (i+1, j)]:
            if 0<=ii<N and 0<=jj<N:
                block[ii][jj] = (block[ii][jj]+num)%4
        return block
    
    for first_rotate in product(range(4), repeat=N):
        block = deepcopy(clockHands)
        ans = 0
        for j,num in enumerate(first_rotate):
            block = rotate(block,(0,j),num)
            ans += num

        for i in range(1,N):
            for j in range(N):
                num = (4-block[i-1][j])%4
                block = rotate(block, (i,j), (num))
                ans += num
        
        if block[-1] == [0 for _ in range(N)]:
            answer = min(answer, ans)
    
    return answer