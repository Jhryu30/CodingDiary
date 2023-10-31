# https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-20055-%EC%BB%A8%EB%B2%A0%EC%9D%B4%EC%96%B4-%EB%B2%A8%ED%8A%B8-%EC%9C%84%EC%9D%98-%EB%A1%9C%EB%B4%87-Python

from collections import deque
import sys

input = sys.stdin.readline

N,K = map(int, input().split())
A = deque(list(map(int, input().split())))
robot = deque([0 for _ in range(N)])

step = 0; result = 0
while result<K:
  A.rotate(1)
  robot.rotate(1)
  robot[-1] = 0

  for i in range(N-2,-1,-1):
    if robot[i] and not robot[i+1] and A[i+1]:
      robot[i+1] = 1
      robot[i] = 0
      A[i+1] -= 1
  
  robot[-1] = 0
  if not robot[0] and A[0]:
    robot[0] = 1
    A[0] -= 1

  step += 1
  result = A.count(0)
  
print(step)