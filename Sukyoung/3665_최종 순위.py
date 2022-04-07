import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    team = list(map(int,input().split()))
    ranking = [0]*(n+1) # 작년 순위
    for i in range(n):
        ranking[team[i]] = i+1
    new_ranking = ranking[::] # 올해 순위
    m = int(input())

    for i in range(m):
        a,b = map(int,input().split())
        if ranking[a] > ranking[b]: # 작년에 a의 순위가 더 낮았던 경우 - 올해는 a가 더 높음
            new_ranking[a]-=1 # a 순위 -1
            new_ranking[b]+=1 # b 순위 +1
        else:
            new_ranking[a] += 1
            new_ranking[b] -= 1

    result = []
    for i in range(1,n+1):  # 등수대로 팀 저장
        if i in new_ranking:
            result.append(new_ranking.index(i))
    if len(result) == n:  # 겹치는 등수 없을 때
        for r in result:
            print(r,end=' ')
    else:  # 겹치는 등수 있을 때 - 순위를 정할 수 없는 경우
        print('IMPOSSIBLE')

# ?인 경우는 뭔지 몰라서 그냥 제출 해봤는데 통과됐다