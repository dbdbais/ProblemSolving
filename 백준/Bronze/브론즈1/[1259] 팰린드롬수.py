st="1"
while(int(st)):
    lst=[]
    st=input()
    for i in range(len(st)):
        lst.append(st[i])
    rst=list(reversed(lst))
    if(int(st)==0):
        continue
    elif(lst==rst):
        print("yes")
    else:
        print("no")

