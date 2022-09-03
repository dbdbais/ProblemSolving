lst=[]
N=int(input())
for i in range(N):
    st=input()
    lst.append(st)
lst=list(set(lst))
lst.sort()
lst.sort(key= lambda x : len(x))
for i in range(len(lst)):
    print(lst[i])
