from collections import deque
import sys
input = sys.stdin.readline


class Queue():
    def __init__(self):
        self.queue = deque()

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        if self.queue:
            print(self.queue.popleft())
        else:
            print(-1)

    def size(self):
        print(len(self.queue))

    def empty(self):
        if self.queue:
            print(0)
        else:
            print(1)

    def front(self):
        if self.queue:
            print(self.queue[0])
        else:
            print(-1)

    def back(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print(-1)


n = int(input())
q1 = Queue()
for _ in range(n):
    st = input().strip().split()

    if len(st) > 1:
        com, num = st[0], int(st[1])
        if com == 'push':
            q1.push(num)

    else:
        com = st[0]
        if com == 'pop':
            q1.pop()
        elif com == 'size':
            q1.size()
        elif com == 'empty':
            q1.empty()
        elif com == 'front':
            q1.front()
        elif com == 'back':
            q1.back()
