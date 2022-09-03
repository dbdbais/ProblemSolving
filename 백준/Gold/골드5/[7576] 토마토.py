import sys
input = sys.stdin.readline
from collections import deque

garden = []
M,N = map(int,input().split())
for _ in range(N):
    garden.append(list(map(int,input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if(garden[i][j]==1):
            queue.append((i,j))
xc=[-1,1,0,0]
yc=[0,0,-1,1]
while queue:
    x,y = queue.popleft()

    for i in range(4):
        qx= x+xc[i]
        qy= y+yc[i]
        if ((0<= qx< N) and (0<= qy < M) and (garden[qx][qy]==0)):
            queue.append((qx,qy))
            garden[qx][qy] = garden[x][y] + 1

res = 0
flag= True

for i in range(N):
    for j in range(M):
        if(res<garden[i][j]):
            res=garden[i][j]
        if(garden[i][j]==0):
            flag = False
            break

if (flag):
    print(res-1)
else:
    print(-1)
