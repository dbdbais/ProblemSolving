import sys
input=sys.stdin.readline

def check(lst,lv,b):
    up=0
    dn=0
    for i in range(N):
        for j in range(M):
            z=lst[i][j] - lv
            if (z>0):
                b+=z
                up += 2*z
            else:
                dn += -z
    if(b<dn):
        return INF
    return up+dn

N,M,B = map(int,input().split())
lst=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
INF=int(1e9)
lo=INF
low=INF
hi=0
high=0
for i in range(N):
    for j in range(M):
        hi=max(hi,lst[i][j])
        low=min(low,lst[i][j])
    lo=min(lo,low)
    high=max(hi,high)

time=INF
height=0
for lv in range(high,low-1,-1):
    tmp=check(lst,lv,B)
    if(time>tmp):
        time=tmp
        height=lv
print(time,height,end=" ")
