import sys
input = sys.stdin.readline

def binary_search(target,data):
    start=0
    end=len(data)-1

    while (start <= end):
        mid=(start+end)//2
        if (data[mid]==target):
            return 1
        elif (data[mid]<target):
            start = mid + 1
        else:
            end= mid -1
    return 0
N = int(input())
lst=list(map(int,input().split()))
lst.sort()
M = int(input())
tmp=list(map(int,input().split()))
for i in range(len(tmp)):
    print(binary_search(tmp[i],lst),end=" ")

