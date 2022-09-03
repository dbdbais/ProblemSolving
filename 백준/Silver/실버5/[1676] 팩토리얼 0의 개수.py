import sys
input=sys.stdin.readline

N=int(input())
res=1
for i in range(N,0,-1):
    res=res*i
res=str(res)
count=0
for i in range(len(res)-1,-1,-1):
    if(res[i]=='0'):
        count +=1
    else:
        break
print(count)