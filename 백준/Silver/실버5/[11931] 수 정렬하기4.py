import sys
input = sys.stdin.readline

n=int(input())
lst=[0]*n
for i in range(n):
    lst[i]=int(input())
lst.sort(reverse=True)
for i in lst:
    print(i)
