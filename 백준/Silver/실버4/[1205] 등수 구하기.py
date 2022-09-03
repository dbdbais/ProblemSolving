import sys
input = sys.stdin.readline

N,Tae,P = map(int,input().split())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
success=0
