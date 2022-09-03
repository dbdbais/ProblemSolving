lst=list(map(int,input().split()))
for i in range(5):
    lst[i]=lst[i]**2
res=sum(lst)%10
print(res)
