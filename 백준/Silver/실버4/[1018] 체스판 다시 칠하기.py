def chess(N,M,lst):
    first=N-8
    second=M-8
    bcount=0
    wcount=0
    for i in range(first,N):
        for j in range(second,M):
            if((i+j)%2==0):
                if(lst[i][j]=='W'):
                    bcount+=1
                else:
                    wcount+=1
            elif((i+j)%2==1):
                if(lst[i][j]=='B'):
                    bcount+=1
                else:
                    wcount+=1
    return min(bcount,wcount)

N,M= map(int,input().split())
lst=[]
for i in range(N):
    st=input()
    lst.append(st)

res=99999
for i in range(8,N+1):
    for j in range(8,M+1):
        res=min(res,chess(i,j,lst))

print(res)

