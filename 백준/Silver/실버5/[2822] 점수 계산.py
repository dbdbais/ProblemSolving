import sys
input = sys.stdin.readline

lst=[0]*8
for i in range(8):
    lst[i]=int(input())
tmp=sorted(lst,reverse=True)
tmp=tmp[:5]
tmp.reverse()
print(sum(tmp))
asc=[]
for i in tmp:
    asc.append(lst.index(i)+1)

asc.sort()
for t in asc:
    print(t,end=" ")

