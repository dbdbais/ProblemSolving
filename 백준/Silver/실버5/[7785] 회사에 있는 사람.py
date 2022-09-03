import sys
input = sys.stdin.readline

dic={}
n=int(input())
for i in range(n):
    st=input().split()
    if(st[1] == "enter"):
        dic[st[0]]=1
    elif(st[1] =="leave"):
        del dic[st[0]]
ans= sorted(dic.keys(),reverse=True)
for i in ans:
    print(i)
