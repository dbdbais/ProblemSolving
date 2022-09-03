import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    dic={}
    cnt=1
    for i in range(n):
        item,typ= input().split()
        dic[typ] = dic.get(typ, []) + [item]
    lst= list(dic.items())
    #print(lst)
    for i in range(len(lst)):
        cnt*=len(lst[i][1])+1

    ans=cnt-1
    print(ans)