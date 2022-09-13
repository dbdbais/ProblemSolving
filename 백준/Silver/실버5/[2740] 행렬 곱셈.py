import sys
input = sys.stdin.readline
a,b = map(int,input().split())
lst1=[]
lst2=[]
for _ in range(a):
    tmp=list(map(int,input().split()))
    lst1.append(tmp)
c,d = map(int,input().split())
for _ in range(c):
    tmp=list(map(int,input().split()))
    lst2.append(tmp)
lst3=[]
for _ in range(a):
    lst3.append([0]*d)

for n in range(a):
    for k in range(d):
        for m in range(b):
            lst3[n][k] += lst1[n][m] * lst2[m][k]
for i in lst3:
    for element in i:
        print(element,end=" ")
    print()
