def num(n):
    res=n
    sm=0
    while(n):
        tmp=(n%10)
        sm +=tmp
        n = n // 10
    return (res+sm)

N=int(input())
for i in range(1,N+1):
        if(num(i)==N):
            print(i)
            break
        elif(i==N):
            print(0)


