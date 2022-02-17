from itertools import combinations

# 입력받기
n,m=map(int, input().split())
maps=[]
for i in range(n):
  maps.append(list(map(int, input().split())))

# 가정집과 치킨집 좌표를 따로 저장한다.
home=[]
chicken=[]
for i in range(n):
  for j in range(n):
    if maps[i][j]==1:
      home.append((i,j))
    elif maps[i][j]==2:
      chicken.append((i,j))

# 살릴 치킨집을 m개만큼 고른다.
pick_chicken=list(combinations(chicken,m))
# 조합별 치킨거리를 저장할 리스트
result=[0]*len(pick_chicken)

for i in home:
  for j in range(len(pick_chicken)):
    # sys.maxsize를 쓰는 곳도 있었구, 적당히 큰 수를 쓰는 곳도 있었음.
    a=100
    for k in pick_chicken[j]:
      temp=abs(i[0]-k[0])+abs(i[1]-k[1])
      a=min(a,temp)
    result[j]+=a

print(min(result))