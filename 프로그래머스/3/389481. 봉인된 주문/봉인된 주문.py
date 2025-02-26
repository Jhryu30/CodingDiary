def solution(n, bans):
    global letter_dict, letter_dict2
    letter_dict = {letter: i for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz', start=1)}
    letter_dict2 = {i: letter for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz', start=1)}
    
    bans = sorted(map(word2int, bans))

    for ban in bans:
        if ban <= n:
            n += 1
        else:
            break

    return int2word(n)


def word2int(word):
    n = 0
    k = len(word)
    for i, w in enumerate(word):
        n += letter_dict[w] * (26 ** (k - i - 1))
    return n


def int2word(n):
    word = ''
    k = 1

    while n > 26 ** k:
        n -= 26 ** k
        k += 1

    for i in range(k, 0, -1):
        base = 26 ** (i - 1)
        letter_idx = (n - 1) // base
        word += letter_dict2[letter_idx + 1]
        n -= letter_idx * base

    return word

