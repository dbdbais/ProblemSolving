import sys
input = sys.stdin.readline

N = int(input())
lst=[]
for _ in range(N):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
cnt=0
for i in range(N):
    cmp=lst[i]
    for j in range(N):
        first=True
        second=True
        if(lst[j][0]<=cmp[0]):   #cmp보다 바닷가로부터의 거리가 더 가깝고
            if(lst[j][1]<cmp[1]):#숙박비가 싸다면
                first=False
                break

        if(lst[j][1]<=cmp[1]):   #cmp보다 숙박비가 더 싸다면
            if(lst[j][0]<cmp[0]):   #거리가 가깝다면
                second=False
                break
    if(first and second):
        cnt +=1
print(cnt)

