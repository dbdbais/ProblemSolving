from collections import deque
import sys
input=sys.stdin.readline #시간초과 문제를 해결하기 위해서 import입력
dq=deque()
def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0
def size():
    return len(dq)

def main():
    N = int(input())
    for i in range(N):
        st=list(input().split())
        if st[0]=="push_front":
            dq.appendleft(st[1])
        elif st[0] == "push_back":
            dq.append(st[1])
        elif st[0] == "pop_front":
            if empty():
                print(-1)
            else:
                print(dq.popleft())
        elif st[0] == "pop_back":
            if empty():
                print(-1)
            else:
                print(dq.pop())
        elif st[0]=="size":
            print(size())
        elif(st[0]=="front"):
            if empty():
                print(-1)
            else:
                print(dq[0])
        elif (st[0] == "back"):
            if empty():
                print(-1)
            else:
                print(dq[len(dq) - 1])
        elif(st[0]=="empty"):
            print(empty())
main()

