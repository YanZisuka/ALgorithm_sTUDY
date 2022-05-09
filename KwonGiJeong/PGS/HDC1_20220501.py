def get_price(bp, bt, it, ap, minutes):
        if minutes > bt:
            if (minutes - bt) % it:
                at = ((minutes - bt) // it) + 1
            else:
                at = (minutes - bt) // it
        else:
            at = 0

        price = bp + (ap * at)

        return price

def solution(passes, minutes):

    answer = get_price(passes[0][0], passes[0][1], passes[0][2], passes[0][3], minutes)

    if len(passes) > 1:
        for i in range(1, len(passes)):
            answer = min(answer, get_price(passes[i][0], passes[i][1], passes[i][2], passes[i][3], minutes))

    return answer