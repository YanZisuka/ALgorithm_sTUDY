import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, st):
        now = self.head
        
        for char in st:
            if char not in now.children:
                now.children[char] = Node(char)
            now = now.children[char]
        now.data = st

    def search(self, st):
        now = self.head
        for char in st:
            if char in now.children:
                now = now.children[char]
            else:
                return False

        if now.data != None:
            return True

    def starts_with(self, prefix):
        now = self.head
        words = []

        for p in prefix:
            if p in now.children:
                now = now.children[p]
            else:
                return None

        now = [now]
        next = []
        while True:
            for v in now:
                if v.data:
                    words.append(v.data)
                next.extend(list(v.children.values()))
            if len(next) != 0:
                now = next
                next = []
            else:
                break

        return words

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cnt = 0
    arr = []
    for _ in range(n):
        arr.append(input().strip())

    trie = Trie()

    for number in arr:
        trie.insert(number)

    for number in arr:
        if len(trie.starts_with(number)) > 1:
            cnt += 1

    if cnt:
        print('NO')
    else:
        print('YES')
