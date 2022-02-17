import sys
sys.stdin = open('input.txt')


def set_floor():
    floor = []
    odd_rooms = []
    even_rooms = []
    for odd in range(1, 400, 2):
        odd_rooms.append(odd)
    for even in range(2, 401, 2):
        even_rooms.append(even)
    floor.append(odd_rooms)
    floor.append([0] * 200)
    floor.append(even_rooms)
    return floor


def set_queue(corridor, odd_rooms, even_rooms):
    for _ in range(n):
        now_room, to_room = map(int, input().split())
        if now_room % 2:  # 현재 방 홀짝 판단
            now_room = odd_rooms.index(now_room)
            if to_room % 2:  # 돌아갈 방 홀짝 판단
                to_room = odd_rooms.index(to_room)
                if now_room < to_room:  # 돌아갈 방이 현재 방보다 오른쪽
                    for i in range(now_room, to_room + 1):
                        corridor[i] += 1
                else:  # 돌아갈 방이 현재 방보다 왼쪽
                    for i in range(now_room, to_room - 1, -1):
                        corridor[i] += 1
            else:
                to_room = even_rooms.index(to_room)
                if now_room < to_room:
                    for i in range(now_room, to_room + 1):
                        corridor[i] += 1
                else:
                    for i in range(now_room, to_room - 1, -1):
                        corridor[i] += 1
        else:
            now_room = even_rooms.index(now_room)
            if to_room % 2:
                to_room = odd_rooms.index(to_room)
                if now_room < to_room:
                    for i in range(now_room, to_room + 1):
                        corridor[i] += 1
                else:
                    for i in range(now_room, to_room - 1, -1):
                        corridor[i] += 1
            else:
                to_room = even_rooms.index(to_room)
                if now_room < to_room:
                    for i in range(now_room, to_room + 1):
                        corridor[i] += 1
                else:
                    for i in range(now_room, to_room - 1, -1):
                        corridor[i] += 1
    return max(corridor)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    floor = set_floor()
    odd_rooms = floor[0]
    corridor = floor[1]
    even_rooms = floor[2]
    
    print(f'#{tc} {set_queue(corridor, odd_rooms, even_rooms)}')