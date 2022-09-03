import sys
input = sys.stdin.readline

from collections import Counter

N=int(input())
lst=[]
for i in range(N):
    tmp=input().rstrip()
    lst.append(tmp)
cnt=list(Counter(lst).items())
cnt.sort(key=lambda x: (-x[1],x[0]))
print(cnt[0][0])