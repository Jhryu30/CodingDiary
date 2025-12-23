def solution(board, moves):
    answer = 0
    N = len(board)
    board_dict = {col+1:[board[N-row-1][col] for row in range(N)] for col in range(N)}
    queue = []

    answer = 0

    for move in moves:
        t = 0
        while board_dict[move] and not t:
            t = board_dict[move].pop()

        prev = queue[-1] if queue else 0

        if t and not t==prev:
            queue.append(t)

        if t and t==prev:
            answer += 2
            queue.pop()

    return answer