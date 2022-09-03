import sys
input=sys.stdin.readline

N=int(input())
card=list(map(int,input().split()))
M=int(input())
search=list(map(int,input().split()))
dic = dict()
for i in card:
    if i in dic:
        dic[i] +=1
    else:
        dic[i]=1

for i in range(M):
    if search[i] in dic:
        print(dic[search[i]],end=" ")
    else:
        print(0,end=" ")
