def solution(n, k, cmd):
    answer = ["X" for _ in range(n)]

    queue = {k: [k-1, k+1] for k in range(1, n-1)}  # cur : [prev,next]
    queue[0], queue[n-1] = [None, 1], [n-2, None]


    current = k
    idxs = []  # (prev,cur,next)


    for command in cmd:
        if command == "C":
            prev, nex = queue[current]
            idxs.append((prev, current, nex))
            if prev is not None:
                queue[prev][1] = nex
            if nex is not None:
                queue[nex][0] = prev
            current = nex if nex is not None else prev


        elif command == "Z":
            prev, cur, nex = idxs.pop()
            if prev is not None:
                queue[prev][1] = cur
            if nex is not None:
                queue[nex][0] = cur
            queue[cur] = [prev, nex]




        else:
            ud, x = command.split(' ')
            x = int(x)
            if ud == "U":
                for _ in range(x):
                    current = queue[current][0]
            else:
                for _ in range(x):
                    current = queue[current][1]

    answer[current] = "O"
    cur1, cur2 = current, current
    while cur1 is not None:
        answer[cur1] = "O"
        cur1 = queue[cur1][1]
    while cur2 is not None:
        answer[cur2] = "O"
        cur2 = queue[cur2][0]
        
    return ''.join(answer)