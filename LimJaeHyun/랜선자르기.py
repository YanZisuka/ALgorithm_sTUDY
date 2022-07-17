yeongsik_lan, lan_needed = map(int, input().split())
lan_length = list(int(input()) for _ in range(yeongsik_lan))

rough_guess = sum(lan_length) // lan_needed
rough_guess_lan = 0

while rough_guess_lan < lan_needed:
    for lan in lan_length:
        rough_guess_lan += lan // rough_guess
    if rough_guess_lan >= lan_needed:
        break
    else:
        rough_guess_lan = 0
        rough_guess -= 1

print(rough_guess)



