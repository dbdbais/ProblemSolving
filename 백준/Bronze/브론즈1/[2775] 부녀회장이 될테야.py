import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    lst = list(range(1,n+1))
    tmp=lst.copy()
    for i in range(k):
        for j in range(1,n+1):
            tmp[j-1]=sum(lst[0:j])
        lst=tmp.copy()
    print(lst[n-1])
