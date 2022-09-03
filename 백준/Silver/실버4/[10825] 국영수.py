import sys
input=sys.stdin.readline
lst=[]
N=int(input())
for i in range(N):
    tmp=list(input().split())
    tmp[1]=int(tmp[1])
    tmp[2]=int(tmp[2])
    tmp[3]=int(tmp[3])
    lst.append(tmp)
lst.sort(key=lambda x : (-x[1],x[2],-x[3],x[0]))
for i in range(N):
    print(lst[i][0])