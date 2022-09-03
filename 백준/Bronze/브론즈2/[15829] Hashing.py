def conv(c):
    return ord(c)-96
sm=0
L=int(input())
st=input()
for i in range(L):
    sm= sm+conv(st[i])*31**i
print(sm%1234567891)

