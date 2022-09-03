N,M = map(int,input().split())
card=list(map(int,input().split()))
res=0
sm=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sm=(card[i]+card[j]+card[k])
            if(sm <= M):
                res=max(sm,res)

print(res)

