n=input()
cnt=0
for i in range(len(n)//10+1):
    for j in range(10):
        if(cnt>=len(n)):
            break
        print(n[cnt],end="")
        cnt +=1
    print()
