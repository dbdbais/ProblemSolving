import sys
input = sys.stdin.readline
a,b=input().split()
res=int(a,2)+int(b,2)
print(bin(res)[2:])
