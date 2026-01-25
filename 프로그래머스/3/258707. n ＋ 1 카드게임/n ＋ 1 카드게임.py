def solution(coin, cards):
    N = len(cards)
    answer = 1

    state = [0] * (N + 1)

    # 초기 손패
    for c in cards[:N // 3]:
        state[c] = 1

    idx = N // 3

    while True:
        # 카드 2장 공개
        if idx >= N:
            break

        c1, c2 = cards[idx], cards[idx + 1]
        idx += 2

        state[c1] = 2
        state[c2] = 2

        used = False

        # (0) 무료 세금 (손 + 손)
        for x in range(1, N + 1):
            if state[x] == 1 and state[N + 1 - x] == 1:
                state[x] = state[N + 1 - x] = 0
                answer += 1
                used = True
                break

        if used:
            continue

        # (1) 1코인 세금 (손 + 공개)
        if coin >= 1:
            for x in range(1, N + 1):
                y = N + 1 - x
                if state[x] == 1 and state[y] == 2:
                    state[x] = state[y] = 0
                    coin -= 1
                    answer += 1
                    used = True
                    break

        if used:
            continue

        # (2) 2코인 세금 (공개 + 공개)
        if coin >= 2:
            for x in range(1, N + 1):
                y = N + 1 - x
                if state[x] == 2 and state[y] == 2:
                    state[x] = state[y] = 0
                    coin -= 2
                    answer += 1
                    used = True
                    break

        if not used:
            break

    return answer
