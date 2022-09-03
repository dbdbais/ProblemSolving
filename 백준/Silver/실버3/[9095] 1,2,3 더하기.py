import sys
input = sys.stdin.readline

lst=[0]*10
lst[0]=1
lst[1]=2
lst[2]=4
for i in range(3,10):
    lst[i]=lst[i-1]+lst[i-2]+lst[i-3]

T = int(input())

for i in range(T):
    n=int(input())
    print(lst[n-1])

