import sys
input=sys.stdin.readline
from collections import deque

N=int(input())
lst=deque(list(range(1,N+1)))
while (lst):
    print(lst.popleft(),end=" ")
    if (lst):
        lst.append(lst.popleft())
