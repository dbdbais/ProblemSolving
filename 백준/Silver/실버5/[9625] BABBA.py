import sys
input = sys.stdin.readline

"""def conv(st):
    temp = ""
    for i in range(len(st)):
        if(st[i]=='A'):
            temp += "B"
        elif(st[i]=="B"):
            temp +="BA"
    return temp

k = int(input())
dp=[0]*(k+1)
dp[0]="A"
for i in range(1,k+1):
    dp[i]=conv(dp[i-1])

print(dp[k].count('A'),dp[k].count("B"),end=" ")        
시간초과 코드 문자열 concat으로 dp배열에 넣어서 count 하지 말고 dp구현 시 점화식만 볼 것
"""
k = int(input())
adp=[0]*46
bdp= [0]*46
adp[0]=1
adp[1]=0
bdp[0]=0
bdp[1]=1

for i in range(2,k+1):
    adp[i] = adp[i-1] + adp[i-2]
    bdp[i] = bdp[i-1] + bdp[i-2]

print(adp[k],bdp[k],end=" ")


