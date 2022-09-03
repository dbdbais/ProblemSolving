import sys
input=sys.stdin.readline

N=int(input())
cnt={}
for i in range(N):
    tmp=int(input())
    if tmp in cnt:
        cnt[tmp] += 1
    else:
        cnt[tmp] = 1
cnt=sorted(cnt.items(),key=lambda x : (-x[1],x[0]))
print(cnt[0][0])