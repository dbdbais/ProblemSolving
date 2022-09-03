import sys
from collections import Counter
input = sys.stdin.readline
n=int(input())
lst=[0]*n
sm=0
for i in range(n):
    lst[i]=int(input())
    sm=sm+lst[i]
print(round(sm/n))
lst.sort()
print(lst[n//2])

tmp=Counter(lst).most_common()
if(len(tmp)>2):
    if(tmp[0][1] == tmp[1][1]):
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

print(lst[-1]-lst[0])