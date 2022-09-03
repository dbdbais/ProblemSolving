import sys
input = sys.stdin.readline

def check(mine,x,y):
    xc = [-1, -1, -1, 0, 0, 1, 1, 1]
    yc = [-1, 0, 1, -1, 1, -1, 0, 1]
    cnt= 0

    for i in range(8):
        fx = x + xc[i]
        fy = y + yc[i]

        if((0<= fx <R) and (0<= fy <C)):
            if(mine[fx][fy] =="*"):
                cnt += 1
    print(cnt,end="")


while True:
    mine=[]
    R,C = map(int,input().split())
    if(R==0 and C==0):
        break

    for _ in range(R):
        st=input().rstrip()
        tmp=list(st)
        mine.append(tmp)
    for i in range(R):
        for j in range(C):
            if(mine[i][j]=="*"):
                print("*",end="")
            else:
                check(mine,i,j)
        print()

