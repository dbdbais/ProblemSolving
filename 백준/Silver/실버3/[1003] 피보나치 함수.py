import sys
input = sys.stdin.readline
z_count=[1,0]
o_count=[0,1]

def fibo(n):
    init=len(z_count)
    if n >= init:
        for i in range(init,n+1):
            z_count.append(z_count[i-1]+z_count[i-2])
            o_count.append(o_count[i-1]+o_count[i-2])
    print(z_count[n], o_count[n])

T=int(input())
for i in range(T):
    n=int(input())
    fibo(n)