import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, foods):
        now = self.head

        for food in foods:
            if food not in now:
                now[food] = {}
            now = now[food]
        now[0] = True

    def travel(self, level, now):
        if 0 in now:
            return

        now_children = sorted(now)

        for child in now_children:
            print('--'*level + child)
            self.travel(level+1, now[child])


n = int(input().strip())
t1 = Trie()
for _ in range(n):
    st = input().split()
    k = st[0]
    foods = st[1:]
    t1.insert(foods)

t1.travel(0, t1.head)
