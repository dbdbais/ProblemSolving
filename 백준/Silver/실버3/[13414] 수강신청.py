import sys
input = sys.stdin.readline

K,L = map(int,input().split()) #K 수강가능인원    L 대기열
dic = {}

for i in range(L):
    tmp = input().rstrip()
    dic[tmp]=i
lst= list(dic.items())

lst.sort(key=lambda x: x[1])
cnt = 0
for i in range(len(lst)):
    print(lst[i][0])
    cnt +=1
    if(cnt==K):
        break