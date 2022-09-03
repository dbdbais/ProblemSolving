k= int(input())
lst=[]
sm=0
for i in range(k):
    tmp=int(input())
    if (tmp==0):
        lst.pop()
    else:
        lst.append(tmp)
#lst.append(0)
for j in range(len(lst)):
    sm=sm+lst[j]
print(sm)
