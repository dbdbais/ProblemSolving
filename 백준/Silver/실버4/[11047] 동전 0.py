import sys
input=sys.stdin.readline
N,K = map(int,input().split())
lst=[0]*N
for i in range(N):
    lst[i]=int(input())
count=0
for j in range(N-1,-1,-1):
    if(K//lst[j]>0):
        count += K//lst[j]
        K -= (K//lst[j])*lst[j]

print(count)