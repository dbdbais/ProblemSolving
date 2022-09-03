import sys
input=sys.stdin.readline
dic={}
N,M = map(int,input().split())
for i in range(N):
    tmp=list(input().split())
    dic[tmp[0]]=tmp[1]
for j in range(M):
    tmp=input()
    tmp=tmp[:-1]
    print(dic[tmp])