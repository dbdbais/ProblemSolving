import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=A+B
ans.sort()
for i in ans:
    print(i,end=" ")