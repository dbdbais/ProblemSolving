import sys
input = sys.stdin.readline
T=int(input())
for i in range(T):
    count = 0
    N,M= map(int,input().split())
    lst=list(map(int,input().split()))
    while(len(lst)):
        if(lst[0]==max(lst)):
            lst.pop(0)
            count += 1
            if(M==0):
                print(count)
                break
            else:
                M=M-1
        else:
            lst.append(lst.pop(0))
            if (M == 0):
                M = len(lst) - 1
            else:
                M = M - 1

