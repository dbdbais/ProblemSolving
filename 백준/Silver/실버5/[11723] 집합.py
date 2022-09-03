import sys
input=sys.stdin.readline
ans=[]
M=int(input())
for i in range(M):
    tmp=list(input().split())
    if(len(tmp)==1):
        if(tmp[0]=="empty"):
            ans=[]
        else:
            ans=list(range(1,21))
    else:
        if(tmp[0]=="add"):
            if int(tmp[1]) not in ans:
                ans.append(int(tmp[1]))

        elif(tmp[0]=="check"):
            if int(tmp[1]) in ans:
                print(1)
            else:
                print(0)
        elif (tmp[0] == "remove"):
            for i in range(len(ans)):
                if(ans[i]==int(tmp[1])):
                    del ans[i]
                    break
        elif (tmp[0] == "toggle"):
            if int(tmp[1]) not in ans:
                ans.append(int(tmp[1]))
            else:
                for j in range(len(ans)):
                    if (ans[j] == int(tmp[1])):
                        del ans[j]
                        break





