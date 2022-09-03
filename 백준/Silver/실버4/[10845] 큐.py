import sys
input=sys.stdin.readline #시간초과 문제를 해결하기 위해서 import입력

class Queue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            dequeued= self.queue[0]
            self.queue=self.queue[1:]
            return dequeued

    def fpeek(self):
        if self.isEmpty():
            return -1
        else:
            peek=self.queue[0]
            return peek

    def rpeek(self):
        if self.isEmpty():
            return -1
        else:
            peek=self.queue[-1]
            return peek
    def size(self):
        return len(self.queue)


def main():
    q=Queue()
    N = int(input())
    for i in range(N):
        st=list(input().split())
        if (len(st) == 2):
            q.enqueue(int(st[1]))
        else:
            if(st[0]=="front"):
                print(q.fpeek())
            elif(st[0]=="back"):
                print(q.rpeek())
            elif(st[0]=="pop"):
                print(q.dequeue())
            elif(st[0]=="empty"):
                if(q.isEmpty()):
                    print(1)
                else:
                    print(0)
            elif(st[0]=="size"):
                print(q.size())

main()

