import sys
N=int(sys.stdin.readline())
lst=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
lst.sort(key= lambda x: (x[0],x[1]))
for i in range(N):
    print(lst[i][0],lst[i][1],sep=" ")
 
