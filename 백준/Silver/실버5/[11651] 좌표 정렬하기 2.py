import sys
input = sys.stdin.readline

N=int(input())
lst=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
lst.sort(key= lambda x: (x[1],x[0]))
for i in range(N):
    print(lst[i][0],lst[i][1],sep=" ")