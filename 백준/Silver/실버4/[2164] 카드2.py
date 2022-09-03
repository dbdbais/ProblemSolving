import sys
import collections
input=sys.stdin.readline

N=int(input())
deck=collections.deque(list(range(1,N+1)))
while(len(deck)>1):
    deck.popleft()
    deck.rotate(-1)
print(deck[0])
