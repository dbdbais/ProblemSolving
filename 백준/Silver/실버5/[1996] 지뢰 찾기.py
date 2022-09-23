import sys
input = sys.stdin.readline

map=[]
n=int(input())
for _ in range(n):
    st=input().rstrip()
    tmp=list(st)
    map.append(tmp)
cordinate=[]
for i in range(n):
    for j in range(n):
        if(map[i][j]!='.'):
            cordinate.append((i,j))
ans = [[0 for _ in range(n)] for _ in range(n)]

xc=[0,0,1,-1,1,1,-1,-1]
yc=[1,-1,0,0,1,-1,1,-1]
for i in range(n):
    for j in range(n):
        cnt = 0
        if(map[i][j]=='.'):
            for k in range(8):
                qx=i+xc[k]
                qy=j+yc[k]

                if((0<=qx<n) and (0<=qy<n) and (map[qx][qy]!='.')):
                    cnt += int(map[qx][qy])
        if(cnt>9):
            ans[i][j]='M'
        else:
            ans[i][j]=str(cnt)
while cordinate:
    x,y = cordinate.pop()
    ans[x][y]='*'

for i in range(n):
    for j in range(n):
        print(ans[i][j],end="")
    print()