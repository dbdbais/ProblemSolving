import sys
input=sys.stdin.readline
def length(x,y,w,h):
    res = 1001
    if(x<=w and y<=h):
        res=min(res,y)
        res=min(res,x)
        res=min(res,h-y)
        res=min(res,w-x)
    else:
        if(w<x):
            res=min(res,x-w)
        if(h<y):
            res=min(res,y-h)
    return res

x,y,w,h=map(int,input().split())
print(length(x,y,w,h))


