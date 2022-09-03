import sys
input=sys.stdin.readline

N,M= map(int,input().split())
dic={}
for i in range(N):
    tmp=input()
    tmp = tmp[:-1]
    dic[i+1]=tmp
    dic[tmp]=i+1

for j in range(M):
    t=input()
    t=t[:-1]
    if(t.isdigit()):
        print(dic[int(t)])
    else:
        print(dic[t])




