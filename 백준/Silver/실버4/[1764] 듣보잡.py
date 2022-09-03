N,M = map(int,input().split())
dt=[]
res=[]
count=0
for i in range(N):
    st=input()
    dt.append(st)
for i in range(M):
    st=input()
    dt.append(st)
dt.sort()
for i in range(len(dt)-1):
    if(dt[i]==dt[i+1]):
        count=count+1
        res.append(dt[i])

res.sort()
print(count)
for i in range(len(res)):
    print(res[i])

