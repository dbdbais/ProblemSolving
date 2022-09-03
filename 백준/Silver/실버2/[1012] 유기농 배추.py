import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀를 이용시 무조건 추가

def DFS(x,y):
    xc=[-1,1,0,0]
    yc=[0,0,-1,1]

    for i in range(4):
        fx=x+xc[i]
        fy=y+yc[i]

        if((0<= fx <M) and (0<= fy <N)):
            if(garden[fx][fy]):
                garden[fx][fy]=0
                DFS(fx,fy)

T=int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    garden = [[0]*N for _ in range(M)]
    for _ in range(K):
        x,y = map(int,input().split())
        garden[x][y] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if(garden[i][j]):
                DFS(i,j)
                cnt +=1
    print(cnt)


