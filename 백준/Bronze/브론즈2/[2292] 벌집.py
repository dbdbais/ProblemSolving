import sys
input=sys.stdin.readline

count=1
i=1
n = int(input())
if(n==1):
    print(i)
else:
    div = 8
    while(True):
        i = i + 1
        if(n//div==0):
            print(i)
            break
        div=div+6*i
