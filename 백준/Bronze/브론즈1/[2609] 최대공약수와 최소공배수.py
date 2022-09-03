def gcd(n,m):
    while(m):
        tmp=n
        n=m
        m=tmp%m
    return n
def lcm(n,m):
    return (n*m)//gcd(n,m)

n,m=map(int,input().split())
x=gcd(n,m)
print(x)
x=lcm(n,m)
print(x)
