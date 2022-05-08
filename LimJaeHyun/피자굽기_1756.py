depth, dow_num = map(int, input().split())
oven_width = list(map(int, input().split()))
dows = list(map(int, input().split()))


pizza_location = [0] * depth
for dow_idx, dow in enumerate(dows):
    for oven_idx, oven in enumerate(oven_width):
        if pizza_location[oven_idx] != 0:
            try:
                pizza_location[oven_idx - 1] = dow_idx + 1
            except IndexError:
                break

        if dow > oven:
            try:
                pizza_location[oven_idx - 1] = dow_idx + 1
                oven_width = oven_width[0:oven_idx+1]
                break
            except IndexError:
                break
        else:
            continue

if len(set(pizza_location)) < dow_num + 1:
    print(0)
if len(set(pizza_location)) == dow_num + 1:
    print(pizza_location.index(dow_num) + 1)


