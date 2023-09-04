def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        temp_arr = sorted(array[i-1:j])
        answer.append(temp_arr[k-1])
    return answer