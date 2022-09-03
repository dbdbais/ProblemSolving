def res(st):
    lcnt=0
    rcnt=0
    suc=1
    ln=len(st)
    for i in range(ln):
        if(st[i]=='('):
            lcnt=lcnt+1
        elif(st[i]==')'):
            rcnt=rcnt+1

        if((lcnt-rcnt)<0):
            suc=0
            break
        if(i==ln-1):
            if(rcnt != lcnt):
                suc=0
        
            
    if(suc==1):
        print("YES")
    else:
        print("NO")


def main():
    lst=[]
    n=int(input())
    for i in range(n):
          st=input()
          res(st)
          
main()
