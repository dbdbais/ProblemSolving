n=int(input())
arr=set(map(int,input().split()))
m=int(input())
comp=list(map(int,input().split()))

for i in comp:
    if i in arr:
        print(1)
    else:
        print(0)
