from collections import deque

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    queue = deque(arr)
    answer.append(arr[0])
    while queue:
        check = queue.popleft()
        if check != answer[-1]:
            answer.append(check)
    return answer