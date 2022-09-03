lst=[]
for i in range(7):
    tmp=int(input())
    if(tmp%2!=0):
        lst.append(tmp)
if(len(lst)==0):
    print(-1)
else:
    print(sum(lst))
    print(min(lst))