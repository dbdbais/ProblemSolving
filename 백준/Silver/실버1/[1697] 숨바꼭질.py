import sys
input = sys.stdin.readline
from collections import deque

def bfs(N,K):
    index=[0]*100001
    queue= deque()
    queue.append(N)
    while(queue):
        x=queue.popleft()
        if(x==K):
            print(index[x])
            break
        else:
            for i in (x-1,x+1,2*x):
                if((0<= i < 100001) and (index[i]==0)):
                    queue.append(i)
                    index[i]=index[x]+1


N,K = map(int,input().split())
bfs(N,K)