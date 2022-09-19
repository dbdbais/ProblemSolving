import sys
input = sys.stdin.readline
from collections import deque
import copy

def BFS(x,y,arr,N,value):
    xc=[0,0,1,-1]
    yc=[-1,1,0,0]

    queue = deque()
    queue.append((x,y))
    arr[x][y]= -1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            qx=x+xc[i]
            qy=y+yc[i]

            if((0<=qx<N)and (0<=qy<N) and (arr[qx][qy]>value)):
                queue.append((qx,qy))
                arr[qx][qy] = -1


N = int(input())
area=[]
mx=-1
ans=1
for _ in range(N):
    tmp=list(map(int,input().split()))
    for i in tmp:
        if(mx<i):
            mx=i
    area.append(tmp)
for v in range(1,mx):
    temparr=copy.deepcopy(area)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if(temparr[i][j]>v):
                BFS(i,j,temparr,N,v)
                cnt += 1
    ans= max(ans,cnt)
    temparr=[]
print(ans)

