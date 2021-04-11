import sys


class stack:
    def __init__(self):
        self.s = []

    def show(self):
        return self.s

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if len(self.s) == 0:
            return -1
        return self.s.pop()

    def size(self):
        return len(self.s)

    def isEmpty(self):
        if len(self.s) == 0:
            return 1
        else:
            return 0

    def top(self):
        if len(self.s) == 0:
            return -1
        return self.s[-1]


a = stack()
n = int(input())
while n > 0:
    n -= 1
    order = sys.stdin.readline().rstrip().split()
    op = order[0]

    if op == 'push':
        a.push(order[1])
    elif op == 'top':
        print(a.top())
    elif op == 'size':
        print(a.size())
    elif op == 'empty':
        print(a.isEmpty())
    elif op == 'pop':
        print(a.pop())
    else:
        print('unexpected order')