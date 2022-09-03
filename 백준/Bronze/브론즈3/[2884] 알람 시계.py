def pnt_Alarm(hr,mn):
    if(mn>=45):
        print(hr,mn-45,end=" ")
    else:
        if(hr ==0):
            print("23",(mn+60)-45,end=" ")
        else:
            print(hr-1,(mn+60)-45,end=" ")
        

def main():
    st = list(map(int,input().split()))
    pnt_Alarm(st[0],st[1])

main()
