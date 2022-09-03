N=int(input())
res=[]
sm=0
arr=list(map(int,input().split()))
arr.sort()
for i in range(N):
    for j in range(i+1):
        sm= sm+ arr[j]
    res.append(sm)
    sm=0
for k in range(N):
    sm=sm+res[k]
print(sm)

