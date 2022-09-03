import sys
input = sys.stdin.readline
while(True):
    lst=[]
    st= input()
    if (st[0] == '.'):
        break
    for i in st:
        if(i=='(' or i== '['):
            lst.append(i)
        elif(i==')'):
            if(len(lst)!=0 and lst[-1]=="("):
                lst.pop()
            else:
                lst.append(i)
                break
        elif(i==']'):
            if(len(lst)!=0 and lst[-1]=="["):
                lst.pop()
            else:
                lst.append(i)
                break
    if(len(lst)==0):
        print("yes")
    else:
        print("no")
