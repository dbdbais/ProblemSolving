res = 0
n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    count=0
    for j in range(1,lst[i]+1):
        if(lst[i]%j == 0):
            count=count+1
    if(count==2):
        res=res+1
print(res)
    
