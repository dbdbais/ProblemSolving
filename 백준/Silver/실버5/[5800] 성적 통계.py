import sys
input = sys.stdin.readline

K=int(input())
for i in range(K):
    lst=list(map(int,input().split()))
    lst=lst[1:]
    lst.sort()
    mx=0
    for j in range(len(lst)-1):
        if(mx<lst[j+1]-lst[j]):
            mx=lst[j+1]-lst[j]
    print("Class "+str(i+1))
    print("Max "+str(max(lst))+", Min "+str(min(lst))+", Largest gap "+str(mx))

