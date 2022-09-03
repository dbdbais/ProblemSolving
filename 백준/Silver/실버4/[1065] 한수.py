import sys
input = sys.stdin.readline

def hansu(n):
    cnt=0
    for i in range(1,n+1):
        if(i<100):
            cnt += 1
        else:
            st=str(i)
            if(int(st[1])-int(st[0]) == int(st[2])-int(st[1])):
                cnt+=1
    print(cnt)

n=int(input())
hansu(n)