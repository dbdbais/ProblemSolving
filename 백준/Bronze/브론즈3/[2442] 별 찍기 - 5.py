import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1+2*i):
        print("*",end="")
    print()
for i in range(n-2,-1,-1):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1+2*i):
        print("*",end="")
    print()