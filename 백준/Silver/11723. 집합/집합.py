import sys

class MyBitmask():
    def __init__(self):
        self.S = 0

    def add(self, x):
        self.S |= (1 << x)

    def remove(self, x):
        self.S &= ~(1 << x)

    def check(self, x):
        print(1 if self.S & (1 << x) > 0 else 0)

    def toggle(self, x):
        self.S ^= (1 << x)

    def all(self):
        self.S = (1 << 20) - 1

    def empty(self):
        self.S = 0

M = int(sys.stdin.readline())
solution = MyBitmask()

for _ in range(M):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        cmd = getattr(solution, command[0])
        cmd(int(command[1]) - 1)
    else:
        cmd = getattr(solution, command[0])
        cmd()
