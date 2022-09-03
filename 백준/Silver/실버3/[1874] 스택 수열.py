import sys
input = sys.stdin.readline
n=int(input())
tmp=[]
sign=[]
cnt = 0
fail = 0
for i in range(n):
    x = int(input())

    while (cnt<x):
        cnt += 1
        tmp.append(cnt)
        sign.append('+')

    if(tmp[-1]==x):
        tmp.pop()
        sign.append('-')
    else:
        fail=1
        break
if(fail):
    print("NO")
else:
    for i in sign:
        print(i)
