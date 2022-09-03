import sys
input=sys.stdin.readline #시간초과 문제를 해결하기 위해서 import입력

top = -1
stack=[]
def command(st):
    global top
    global stack
    if(len(st)==2): #push연산 일 때
        stack.append(int(st[1]))
        top=top+1
    elif(st[0]=="pop"):
        if(top==-1):
            print(-1)
        else:
            top=top-1
            print(stack.pop())
    elif(st[0]=="size"):
        print(len(stack))

    elif(st[0]=="empty"):
        if(top==-1):
            print(1)
        else:
            print(0)
    elif(st[0]=="top"):
        if(top!= -1):
            print(stack[top])
        else:
            print(-1)
            
def main():
    n=int(input())
    for i in range(n):
        st=input().split()
        command(st)

main()
