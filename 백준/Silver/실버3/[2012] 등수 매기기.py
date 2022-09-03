import sys
input = sys.stdin.readline

n=int(input())
ans=[0]*n
for i in range(n):
    ans[i]=int(input())
ans.sort()
rnk=list(range(1,n+1))

res=0
for i in range(n):
    res= res+ abs(rnk[i]-ans[i])

print(res)

