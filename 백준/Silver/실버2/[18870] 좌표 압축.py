import sys
input = sys.stdin.readline

N=int(input())
lst=list(map(int,input().split()))
tmp=sorted(list((set(lst))))
rank={}
for i in range(len(tmp)):
    rank[tmp[i]]=i

for i in lst:
    print(rank[i],end=" ")

