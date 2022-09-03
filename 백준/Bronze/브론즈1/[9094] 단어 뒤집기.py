import sys
input = sys.stdin.readline

n=int(input())
    lst=list(input().split())
    for j in range(len(lst)):
        for k in range(len(lst[j])-1,-1,-1):
            print(lst[j][k],end="")
        print(end=" ")
