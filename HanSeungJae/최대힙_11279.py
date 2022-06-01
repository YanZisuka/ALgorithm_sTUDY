import sys
from collections import deque
from heapq import *
input = sys.stdin.readline


class MaxHeap:

    def __init__(self):
        self.tree = deque([None])

    def push(self, num):
        self.tree.append(num)
        idx = len(self.tree) - 1

        while True:
            parent = idx // 2
            if self.tree[parent] == None: return
            if self.tree[idx] > self.tree[parent]:
                self.tree[idx], self.tree[parent] = self.tree[parent], self.tree[idx]
                idx //= 2
            else: return

    def pop(self):
        if len(self.tree) == 1:
            print(0)
            return
        self.tree.popleft()
        print(self.tree.popleft())
        if len(self.tree) > 0:
            last = self.tree.pop()
            self.tree.appendleft(last)
        self.tree.appendleft(None)
        idx = 1
        n = len(self.tree)

        while True:
            left, right = idx * 2, idx * 2 + 1
            if left <= n - 1 and right <= n - 1:
                if self.tree[left] > self.tree[idx] and self.tree[right] > self.tree[idx]:
                    change = left if self.tree[left] >= self.tree[right] else right
                    self.tree[change], self.tree[idx] = self.tree[idx], self.tree[change]
                    idx = change
                elif self.tree[left] > self.tree[idx]:
                    self.tree[left], self.tree[idx] = self.tree[idx], self.tree[left]
                    idx = left
                elif self.tree[right] > self.tree[idx]:
                    self.tree[right], self.tree[idx] = self.tree[idx], self.tree[right]
                    idx = right
                else: return
            elif left <= n - 1:
                if self.tree[left] > self.tree[idx]:
                    self.tree[left], self.tree[idx] = self.tree[idx], self.tree[left]
                    idx = left
                else: return
            else: return


h = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(h) == 0: print(0)
        else:
            print(heappop(h)[1])
    else: heappush(h, (-x, x))
