import math
import sys
input = sys.stdin.readline

n=int(input())
root=int(math.sqrt(n))
dp=[0]*(root+1)
for i in range(1,len(dp)):
    dp[i]=(i)**2
cnt = 0
print(dp)
while (n):
    tmp= int(math.sqrt(n))
    print(tmp,end="^2 ")
    n = n - dp[tmp]
    cnt +=1
print()
print(cnt)




