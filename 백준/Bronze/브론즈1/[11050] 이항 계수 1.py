N,K = map(int,input().split())
bunja=1
bunmo=1
for i in range(K):
    bunja=bunja*(N-i)
    bunmo=bunmo*(i+1)
print(bunja//bunmo)
    
