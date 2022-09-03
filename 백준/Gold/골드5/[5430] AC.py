import sys
input = sys.stdin.readline
from collections import deque

T=int(input())
for i in range(T):
    cmd=input().rstrip()
    en=int(input())
    element=input()
    element=element[1:-2]
    lst = element.split(",")
    if(en==0):
        lst=[]

    if(lst):
        for k in range(len(lst)):
            lst[k]=int(lst[k])
    lst=deque(lst)
    rcount = 0
    fail = 0
    for j in range(len(cmd)):
        if(cmd[j]=='R'):
            rcount += 1
        else:
            if(lst):
                if(rcount%2==0):
                    lst.popleft()
                else:
                    lst.pop()
            else:
                fail=1
                break


    if(fail==1):
        print("error")
    else:
        if(rcount%2==0):
            print("[",end="")
            for i in range(len(lst)):
                if(i==len(lst)-1):
                    print(lst[i],end="")
                else:
                    print(lst[i],end=",")
            print("]")
        else:
            print("[", end="")
            for i in range(len(lst)-1,-1,-1):
                if(i==0):
                    print(lst[i], end="")
                else:
                    print(lst[i], end=",")
            print("]")


