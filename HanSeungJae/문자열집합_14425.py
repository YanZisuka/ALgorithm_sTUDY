"""
PyPy3
"""
import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        now = self.head

        for char in word:
            if char not in now.children:
                now.children[char] = Node(char)
            now = now.children[char]
        now.data = word

    def search(self, word):
        now = self.head

        for char in word:
            if char in now.children:
                now = now.children[char]
            else:
                return False

        if now.data != None:
            return True


n, m = map(int, input().split())
t1 = Trie()
ans = 0

for _ in range(n):
    t1.insert(input().strip())

for _ in range(m):
    if t1.search(input().strip()):
        ans += 1

print(ans)