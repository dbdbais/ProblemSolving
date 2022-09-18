import sys
import copy
from collections import deque
input = sys.stdin.readline

def BFS(x,y,array,N):
    xc=[-1,1,0,0]
    yc=[0,0,-1,1]
    value=array[x][y]
    queue = deque()
    queue.append((x,y))
    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            qx = x + xc[i]
            qy = y + yc[i]
            if((0<= qx <N)and(0<= qy <N) and (array[qx][qy]==value)):
                queue.append((qx,qy))
                array[qx][qy] = 0

N = int(input())
picture=[]
for _ in range(N):
    tmp=list(input().rstrip())
    picture.append(tmp)

plist = copy.deepcopy(picture)

for i in range(N):
    for j in range(N):
        if(plist[i][j]=="G"):
            plist[i][j]="R"

cnt=[0]*2
for i in range(N):
    for j in range(N):
        if(picture[i][j] != 0):
            BFS(i,j,picture,N)
            cnt[0] += 1
for i in range(N):
    for j in range(N):
        if(plist[i][j] != 0):
            BFS(i,j,plist,N)
            cnt[1] += 1
for t in cnt:
    print(t,end=" ")