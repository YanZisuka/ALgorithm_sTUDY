import sys
sys.stdin = open('input.txt')

dy = [0.5, -0.5, 0, 0]
dx = [0, 0, -0.5, 0.5]


def solution():
    global ans
    
    for _ in range(4000):
        if len(atoms) < 2:
            return
        
        for i in range(n):  # 원자들 이동
            if atoms.get(i):
                x, y = atoms[i][0], atoms[i][1]
                dir = atoms[i][2]
                atoms[i][0] = x + dx[dir]
                atoms[i][1] = y + dy[dir]
                
                if atoms[i][0] < -1000 or atoms[i][0] > 1000 or atoms[i][1] < -1000 or atoms[i][1] > 1000:
                    del atoms[i]
                    
        collisions = {tuple(atoms[i][:2]): [] for i in atoms.keys()}  # 원자들의 현 좌표 (충돌 가능성 있는 좌표들)
        
        for i in atoms.keys():
            collisions[tuple(atoms[i][:2])].append(i)  # 충돌 가능성 있는 좌표들에 존재하는 원자들 append
                
        for i in collisions.keys():
            if len(collisions[i]) > 1:  # 한 좌표에 원자 2개 이상이면 충돌한 것이므로 처리
                for j in collisions[i]:
                    k = atoms[j][3]
                    ans += k
                    del atoms[j]
                

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    atoms = {i: 0 for i in range(n)}
    ans = 0
    
    for i in range(n):
        x, y, dir, k = map(int, input().split())
        atoms[i] = [x, y, dir, k]
    
    solution()
    print(f'#{tc} {ans}')