import sys
input = sys.stdin.readline
def check(x,y,n):
    extract = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if(paper[i][j] != extract):
                check(x,y,n//2)
                check(x+n//2,y,n//2)
                check(x , y+n//2, n // 2)
                check(x + n//2, y+n//2, n // 2)
                return
    if(extract == 1):
        color.append(1)
    else:
        color.append(0)

color = []
n =int(input())
paper=[list(map(int,input().split()))for _ in range(n)]

check(0,0,n)
print(color.count(0))
print(color.count(1))