import sys
input=sys.stdin.readline
n=int(input())
lst=[0]*300
dp=[0]*300

for i in range(n):
    lst[i]=int(input())
dp[0]=lst[0]
dp[1]=max(lst[0]+lst[1],lst[1])
dp[2]= max(lst[0]+lst[2],lst[1]+lst[2])
for i in range(3,n):
    dp[i]=max(dp[i-2]+lst[i],dp[i-3]+lst[i]+lst[i-1])
print(dp[n-1])