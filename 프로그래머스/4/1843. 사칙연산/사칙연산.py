def solution(arr):
    
    result_dict = {}
    
    def mini_solution(arr):
        if ''.join(arr) in result_dict:
            return result_dict[''.join(arr)]
        if len(arr) == 1:
            return int(arr[0]), int(arr[0])

        min_val = float('inf')
        max_val = float('-inf')

        for i, eqn in enumerate(arr):
            if eqn in ["+", "-"]:
                left_min, left_max = mini_solution(arr[:i])
                right_min, right_max = mini_solution(arr[i + 1:])

                if eqn == "+":
                    max_val = max(max_val, left_max + right_max)
                    min_val = min(min_val, left_min + right_min)
                else:
                    max_val = max(max_val, left_max - right_min)
                    min_val = min(min_val, left_min - right_max)
                    
        result_dict[''.join(arr)] = [min_val,max_val]
        return min_val, max_val

    _, answer = mini_solution(arr)
    
    return answer
