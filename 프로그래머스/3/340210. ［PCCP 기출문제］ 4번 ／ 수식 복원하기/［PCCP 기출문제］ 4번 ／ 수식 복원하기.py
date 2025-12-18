def solution(expressions):

    def to_base(num, base):
        if num == 0:
            return "0"
        sign = '-' if num < 0 else ''
        num = abs(num)
        res = ''
        while num > 0:
            num, r = divmod(num, base)
            res = str(r) + res
        return sign + res

    def eval_true(expression, base):
        left, c = expression.split(' = ')
        op = '+' if '+' in left else '-'
        a, b = left.split(f' {op} ')
        try:
            a_n, b_n, c_n = int(a, base), int(b, base), int(c, base)
            return (a_n + b_n if op == '+' else a_n - b_n) == c_n
        except:
            return False

    def calc_x(expression, base):
        left, _ = expression.split(' = ')
        op = '+' if '+' in left else '-'
        a, b = left.split(f' {op} ')
        a_n, b_n = int(a, base), int(b, base)
        res = a_n + b_n if op == '+' else a_n - b_n
        return to_base(res, base)

    def min_base_of(expr):
        digits = [int(ch) for ch in expr if ch.isdigit()]
        return max(digits) + 1 if digits else 2

    n_cand = list(range(2, 10))
    targets = []

    for expr in expressions:
        n_cand = [n for n in n_cand if n >= min_base_of(expr)]
        if 'X' in expr:
            targets.append(expr)
        else:
            n_cand = [n for n in n_cand if eval_true(expr, n)]

    answer = []
    for expr in targets:
        results = {calc_x(expr, n) for n in n_cand}
        result = results.pop() if len(results) == 1 else '?'
        answer.append(expr[:-1] + result)

    return answer
