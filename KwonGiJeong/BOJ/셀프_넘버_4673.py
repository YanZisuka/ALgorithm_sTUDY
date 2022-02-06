def d(number):
    total = number
    while (number > 0):
        total += number % 10
        number = number // 10
        if total > 10000:
            break
        elif number == 0:
            return total

ds = []
for i in range(1, 10001):
    ds.append(d(i))

for i in range(1, 10001):
    if not i in ds:
        print(i)