import sys
input=sys.stdin.readline
def address(N):
    count = len(N)
    for i in range(len(N)-1):
        if(N[i]=='1'):
            count+=2
        elif(N[i]=='0'):
            count+=4
        else:
            count+=3
    print(count)
N=input()
while(int(N)):
    address(N)
    N=input()
