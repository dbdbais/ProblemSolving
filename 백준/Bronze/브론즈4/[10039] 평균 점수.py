import sys
input=sys.stdin.readline
lst=[]
for i in range(5):
    tmp=int(input())
    if(tmp>40):
        lst.append(tmp)
    else:
        lst.append(40)
print(sum(lst)//5)