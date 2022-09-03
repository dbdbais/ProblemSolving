import sys
input=sys.stdin.readline
M=int(input())
N=int(input())
lst=[]
while(M<N+1):
    count = 0
    if(M<2):
        M = 2
    for i in range(2,M+1):
        if(count>1):
            break
        if(M%i==0):
            count+=1
    if(count==1):
        lst.append(M)
    M += 1

if(len(lst)>0):
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
