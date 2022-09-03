def stick(x):
    count = 0
    d=64
    while(x != 0):
        if((x-d)>=0):
            x=x-d
            count= count+1
        d=d//2
    print(count)

def main():
    x=int(input())
    stick(x)

main()
