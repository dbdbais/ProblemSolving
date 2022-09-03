def main():
    n,k=map(int,input().split())
    arr=[]
    res=[]
    count = 0
    for i in range(n):
        arr.append(i+1)
    for i in range(n):
        count= (count+k-1)%len(arr)
        res.append(arr[count])
        del arr[count]
    print("<",end="")
    for r in range(n-1):
        print((res[r]),end=", ")
    print(res[-1],end=">")

main()
