def solution(key, lock):
    M,N = len(key),len(lock)
    
    missing = N*N - sum([sum(lock[row]) for row in range(N)])
    key_missing = sum([sum(key[row]) for row in range(M)])
    if M==1:
        return True if missing<=1 else False
    if missing>key_missing:
        return False
    
    new_lock = [[0 for _ in range(3*N)] for _ in range(3*N)]
    for i in range(N):
        for j in range(N):
            new_lock[N+i][N+j] = lock[i][j]
    lock = new_lock[:]
    
    # print(*lock, sep='\n')
    def match(my_key,start_i,start_j):
        nonlocal lock
        for prev_i in range(N,start_i):
            if 0 in lock[prev_i][N:2*N]:
                return False
            
        for i in range(M):
            if start_i+i>=N and start_i+i<2*N:
                if 0 in lock[start_i+i][N:start_j]:
                    return False
                if 0 in lock[start_i+i][start_j+M:2*N]:
                    return False
            for k in range(M):  # 변수명을 j에서 k로 변경
                if start_i + i >= N and start_i + i < 2 * N and start_j + k >= N and start_j + k < 2 * N:
                    if lock[start_i + i][start_j + k] and my_key[i][k]:
                        return False
                    if not lock[start_i + i][start_j + k] and not my_key[i][k]:
                        return False
            

        for post_i in range(start_i+M,2*N):
            if 0 in lock[post_i][N:2*N]:
                return False
        
        return True
    
    key0 = key[:]
    key1 = list(zip(*key0[::-1]))
    key2= list(zip(*key1[::-1]))
    key3 = list(zip(*key2[::-1]))
        
    for start_i in range(N-M+1,2*N):
        for start_j in range(N-M+1,2*N):
            for my_key in [key0, key1, key2, key3]:
                if match(my_key, start_i, start_j):
                    return True
            
    return False