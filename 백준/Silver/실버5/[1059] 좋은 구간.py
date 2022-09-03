def sol(lst,n,L):
    mn=-1
    mx=-1
    for i in range(L):
        if(n<lst[i]):
            mx=lst[i]
            mn=lst[i-1]
            if(mx<mn):
                mn= 0
            break
    
    if(n in lst):
        print(0)
    else:
        print((n-mn-1)*(mx-n)+(mx-n-1))



def main():
    L= int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    n=int(input())
    sol(lst,n,L)


main()
