import sys
input = sys.stdin.readline

n,a = map(int,input().split())
lst= list(map(int,input().split()))
lst.sort()
print(lst[a-1])