N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
sm=0
for i in range(N):
    sm=sm+A[i]*B[i]

print(sm)


