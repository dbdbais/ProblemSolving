import sys
input = sys.stdin.readline

n = int(input())
mine=[]     #지뢰의 원본을 입력받을 리스트
for _ in range(n):
    tmp=list(input().rstrip())
    mine.append(tmp)
coordinate=[]       # 좌표를 입력받을 리스트
for _ in range(n):
    tmp=list(input().rstrip())
    coordinate.append(tmp)
stack=[]        #좌표를 저장할 스택
for i in range(n):
    for j in range(n):
        if(coordinate[i][j]=='x'):      #x 즉 열린 좌표는 스택에 추가
            stack.append((i,j))
ans=[['.' for _ in range(n)] for _ in range(n)]

xc=[-1,1,0,0,1,1,-1,-1]
yc=[0,0,1,-1,1,-1,1,-1]
flag = True     #지뢰를 밟았는지 판별해주는 bool형 변수
while stack:    #stack이 empty할 때까지 반복
    x,y = stack.pop()
    if(mine[x][y]=='*'):    #지뢰를 밟은 경우
        flag=False
    else:
        cnt = 0
        for i in range(8):
            qx=x+xc[i]
            qy=y+yc[i]
            if((0<=qx<n) and (0<=qy<n) and (mine[qx][qy]=='*')):    #최솟값과 최댓값을 벗어나지 않고 주위 지뢰를 찾았다면
                cnt += 1    #cnt를 1 증가
        ans[x][y] =str(cnt)
if flag:    #지뢰를 밟지 않았다면
    for i in range(n):
        for j in range(n):
            print(ans[i][j],end="")
        print()
else:
    bomb=[]
    for i in range(n):
        for j in range(n):
            if(mine[i][j]=="*"):
                bomb.append((i,j))
    while bomb:
        x,y= bomb.pop()
        ans[x][y]='*'
    for i in range(n):
        for j in range(n):
            print(ans[i][j],end="")
        print()
