import sys
input = sys.stdin.readline
from collections import deque

def bfs(apart,i,j,N):
    queue=deque()
    cnt=1
    xc=[0,0,1,-1]
    yc=[-1,1,0,0]
    queue.append((i,j))
    apart[i][j] = -1
    while(queue):
        x,y= queue.popleft()
        for i in range(4):
            qx=x+xc[i]
            qy=y+yc[i]
            if((0<=qx<N)and(0<=qy<N)and(apart[qx][qy]==1)):
                apart[qx][qy]=-1
                queue.append((qx,qy))
                cnt += 1
    return cnt

N= int(input())
danzi=[]
apart=[]
for i in range(N):
    st=input().rstrip()
    tmp=list(map(int,st))
    apart.append(tmp)

for i in range(N):
    for j in range(N):
        if(apart[i][j]==1):
            danzi.append(bfs(apart,i,j,N))

danzi.sort()

print(len(danzi))

for i in danzi:
    print(i)