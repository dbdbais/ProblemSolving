import sys
input = sys.stdin.readline

N=int(input())
first=1
count=0
while True:
    if"666" in str(first):
        count +=1
    if(count==N):
        print(first)
        break
    first +=1
