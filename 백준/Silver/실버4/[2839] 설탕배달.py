def bongji(N):
    error = -1
    n=N//5
    for i in range(n,-1,-1):
        if((N-5*i)%3==0):
            print(i+(N-5*i)//3)
            error = 0
            break
    
    if(error != 0):
        print(-1)


def main():
    N=int(input())
    bongji(N)

main()
