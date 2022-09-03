def combination(n,m):
    bunza = 1
    bunmo = 1
    for i in range(n):
        bunza = bunza * (m-i)
        bunmo = bunmo * (n-i)
    print(bunza//bunmo)


N=int(input())
for i in range(N):
    n,m = map(int,(input().split()))
    combination(n,m)
    
