a, b, v = map(int, input().split())

if (v-b) % (a-b):
    n =  (v-b) // (a-b) + 1
else:
    n =  (v-b) // (a-b)

print(n)