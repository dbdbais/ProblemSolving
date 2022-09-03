import sys
input=sys.stdin.readline

n=int(input())
lst=[]
for i in range(n):
    t=int(input())
    lst.append(t)
lst.sort()

for i in lst:
    print(i)