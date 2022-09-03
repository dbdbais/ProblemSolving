import sys
input = sys.stdin.readline

n=int(input())
lst=[0]*n
for i in range(n):
    lst[i]=int(input())
lst.sort()
for i in range(n):
    print(lst[i])
