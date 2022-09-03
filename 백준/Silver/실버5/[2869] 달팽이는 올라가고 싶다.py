def snail(A,B,V):
    x=(V-B)/(A-B)
    if(x==int(x)):
        print(int(x))
    else:
        print(int(x)+1)
        
A,B,V=map(int,input().split())
snail(A,B,V)
    
