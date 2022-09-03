import sys

n=int(sys.stdin.readline())
lst=[0]*10001

for i in range(n):
    t=int(sys.stdin.readline())
    lst[t] = lst[t]+1

for i in range(10001):
    if(lst[i] != 0):
        for j in range(lst[i]):
            print(i)
