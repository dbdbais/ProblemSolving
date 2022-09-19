import sys
input = sys.stdin.readline
from collections import deque
def BFS(x,y,arr,w,h):
    xc=[-1,1,0,0,-1,1,-1,1]
    yc=[0,0,-1,1,-1,1,1,-1]
    queue=deque()
    queue.append((x,y))
    arr[x][y]=0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            qx=x+xc[i]
            qy=y+yc[i]

            if ((0<=qx<h) and (0<=qy<w) and arr[qx][qy]==1):
                queue.append((qx,qy))
                arr[qx][qy] = 0
while True:
    w,h = map(int,input().split())
    cnt = 0
    if(w or h):
        island=[]
        for _ in range(h):
            tmp=list(map(int,input().split()))
            island.append(tmp)
        for i in range(h):
            for j in range(w):
                if(island[i][j]==1):
                    BFS(i,j,island,w,h)
                    cnt +=1
        print(cnt)
    else:
        break