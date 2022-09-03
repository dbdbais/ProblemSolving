def ACM(H,W,N):
    width=((N-1)//H)+1 #H 손님이 가게 될 호수
    height=((N-1)%H)+1  #손님이 가게 될 층수
    print(height*100+width)

def main():
    T=int(input())
    for i in range(T):
        H,W,N=map(int,input().split())
        ACM(H,W,N)

main()