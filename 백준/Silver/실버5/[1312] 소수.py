import sys
input = sys.stdin.readline

A,B,N = map(int,input().split())
for i in range(N):
    A = (A%B) *10
    res=A//B
print(res)