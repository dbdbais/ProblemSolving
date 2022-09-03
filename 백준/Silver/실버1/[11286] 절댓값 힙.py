import heapq
import sys
input = sys.stdin.readline

N=int(input())
lst=[]
for i in range(N):
    tmp=int(input())
    if(tmp == 0):
        if(lst):
            print(heapq.heappop(lst)[1])
        else:
            print(0)
    else:
        heapq.heappush(lst,(abs(tmp),tmp))

