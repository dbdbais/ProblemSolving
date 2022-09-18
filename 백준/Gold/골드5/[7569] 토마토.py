import sys
input = sys.stdin.readline
from collections import deque

garden = []
M,N,H = map(int,input().split())        #3차원 배열로 푼다 쌓여있는 토마토상자
for i in range(H):
    tmp=[]
    for j in range(N):
        tmp.append(list(map(int,input().split())))
    garden.append(tmp)

xc=[-1,1,0,0,0,0]
yc=[0,0,-1,1,0,0]
zc=[0,0,0,0,-1,1]

queue = deque()
for i in range(H):          #리스트를 돌아다니면서 1인 값을 전부 큐에 집어넣음
    for j in range(N):
        for k in range(M):
            if(garden[i][j][k]==1):
                queue.append((i,j,k))

while queue:
    x,y,z = queue.popleft()

    for i in range(6):
        qx= x+xc[i]
        qy= y+yc[i]
        qz= z+zc[i]
        if ((0<= qx< H) and (0<= qy < N) and(0<=qz <M) and (garden[qx][qy][qz]==0)):
            queue.append((qx,qy,qz))
            garden[qx][qy][qz] = garden[x][y][z] + 1

res = 0
flag= True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if(res<garden[i][j][k]):        #가장 최댓값을 res의 저장
                res=garden[i][j][k]
            if(garden[i][j][k]==0):         #하나라도 0이 나오면 토마토가 전부 익지 못했다는 것 flag값 바꾸고 반복문 break
                flag = False
                break

if (flag):
    print(res-1)
else:
    print(-1)
