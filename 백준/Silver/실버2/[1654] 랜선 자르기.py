import sys
input=sys.stdin.readline
K,N = map(int,input().split())
lst=[]
for i in range(K):
    t=int(input())
    lst.append(t)
last=max(lst)
first=1
while (first <=last):
    mid=(first+last)//2
    ans=0
    for i in range(K):
        ans += lst[i]//mid

    if (ans >= N):
        first=mid+1
    else:
        last=mid-1
print(last)
