import sys
input = sys.stdin.readline

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.stack))

    def empty(self):
        if self.stack:
            print(0)
        else:
            print(1)

    def top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)

n = int(input())
s1 = Stack()

for _ in range(n):
    command = input().strip().split()

    if len(command) > 1:
        command, num = command[0], int(command[1])
        if command == 'push':
            s1.push(num)

    else:
        command = command[0]
        if command == 'pop':
            s1.pop()
        elif command == 'size':
            s1.size()
        elif command == 'empty':
            s1.empty()
        elif command == 'top':
            s1.top()
    