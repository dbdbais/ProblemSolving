import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

xc=[-1,1,0,0]
yc=[0,0,-1,1]

maze=[]

for _ in range(N):
    st=input().rstrip()
    tmp=list(map(int,st))
    maze.append(tmp)

queue = deque()
queue.append((0,0))
while queue:

    x,y = queue.popleft()

    for i in range(4):
        qx = x+xc[i]
        qy = y+yc[i]

        if((0<= qx < N) and(0<= qy <M) and (maze[qx][qy] == 1)):
            queue.append((qx,qy))
            maze[qx][qy]= maze[x][y]+1

print(maze[N-1][M-1])

