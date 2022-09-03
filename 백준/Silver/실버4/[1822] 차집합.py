import sys
input = sys.stdin.readline

na,nb= map(int,input().split())
la=list(map(int,input().split()))
lb=list(map(int,input().split()))
la=set(la)
lb=set(lb)
ans= la-lb
if(ans):
    print(len(ans))
    for i in sorted(ans):
        print(i,end=" ")
else:
    print(0)