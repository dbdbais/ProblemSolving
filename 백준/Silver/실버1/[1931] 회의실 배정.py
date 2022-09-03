import sys
input = sys.stdin.readline

N= int(input())
lst=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
lst.sort(key=lambda x: (x[1],x[0]))
ans=[]
end=lst[0][1]
ans.append(lst[0])
for i in range(1,len(lst)):
    if (lst[i][0]>=end):
        ans.append(lst[i])
        end=lst[i][1]
print(len(ans))