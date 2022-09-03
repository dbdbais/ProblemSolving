import sys
input = sys.stdin.readline
N,M = map(int,input().split())
lst=list(map(int,input().split()))
partial=[0]
sm=0
for elements in lst:
    sm += elements
    partial.append(sm)
for a in range(M):
    i,j = map(int,input().split())
    print(partial[j]-partial[i-1])

