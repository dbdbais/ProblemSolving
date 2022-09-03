import sys
input = sys.stdin.readline
lst=[]
n=int(input())
for i in range(n):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
ans=[]
for i in range(n):
    count=1
    for j in range(n):
        if(lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]):
            count +=1
    ans.append(count)
for i in ans:
    print(i,end=" ")