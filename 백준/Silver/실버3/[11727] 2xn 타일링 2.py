import sys
input = sys.stdin.readline

n=int(input())
ans=[0,1,3]
for i in range(3,n+1):
    ans.append(ans[i-1] + ans[i-2] * 2)
print(ans[n]%10007)