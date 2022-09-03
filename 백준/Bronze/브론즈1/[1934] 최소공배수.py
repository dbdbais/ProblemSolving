def gcd(n,m):
    while(m):
        tmp=n
        n=m
        m=tmp%m
    return n
def lcm(n,m):
    return (n*m)//gcd(n,m)

T=int(input())
for i in range(T):
    A,B = map(int,input().split())
    tmp=lcm(A,B)
    print(tmp)