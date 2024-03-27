from collections import deque

gear = [deque(map(int,list(input()))) for _ in range(4)]

for _ in range(int(input())):
  gear_num, direction = map(int, input().split(' '))
  gear_num -= 1

  connected = [gear[i][2]==gear[i+1][-2] for i in range(3)]

  dirR = direction
  for gearR in range(gear_num+1,4):
    dirR *= -1
    if not connected[gearR-1]:
      gear[gearR].rotate(dirR)
    else:
      break

  dirL = direction
  for gearL in range(gear_num-1,-1,-1):
    dirL *= -1
    if not connected[gearL]:
      gear[gearL].rotate(dirL)
    else:
      break

  gear[gear_num].rotate(direction)

answer = sum([gear[i][0]*2**i for i in range(4)])
print(answer)