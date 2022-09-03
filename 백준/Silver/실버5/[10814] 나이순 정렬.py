lst=[]
res=[]
N=int(input())
for i in range(N):
    lst= input().split()
    lst[0]=int(lst[0])
    res.append(lst)
res.sort(key=lambda x : x[0])
for i in range(N):
    print(res[i][0],res[i][1],sep=" ")
