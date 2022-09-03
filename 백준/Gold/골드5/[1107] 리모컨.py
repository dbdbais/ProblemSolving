import sys
input=sys.stdin.readline

def remote_control(N,M,lst):
    res=[]
    count=0
    number=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(lst)):
        if(lst[i] in number):
            number.remove(lst[i])
    st=str(N)
    asc=-1
    for i in range(len(st)):#N의 길이만큼 반복
        for j in range (len(number)): #들어있는 number만큼 반복
            if(number[j]==int(st[i]) and asc!= -1): #st[i]가 number리스트에 존재하는 경우
                count += 1
                res.append(number[j])
                break
            elif (asc == 1):  # 전 수가 작았을 경우 // 무조건 큰 수를 불러온다
                count += 1
                res.append(number[-1])
                break

            elif (asc == 0):  # 전 수가 컸을 경우 // 무조건 작은 수를 불러온다
                count += 1
                res.append(number[0])
                break


            else: #첫번 쨰 인 경우
                if(number[j]>int(st[i])):
                    if(j==0 and number[j]>int(st[i])):
                        count+=1
                        res.append(number[j])
                        asc=0
                        break

                    elif((number[j]-int(st[i]))>=(int(st[i])-number[j-1])): #number[j-1] 낮은수가 입력
                        count += 1
                        res.append(number[j-1])
                        asc=1
                        break
                    elif((number[j]-int(st[i]))<(int(st[i])-number[j-1])):
                        count += 1
                        res.append(number[j]) #높은 수 가 더 가까워 입력 되어짐
                        asc=0
                        break
                elif(j==len(number)-1):
                    count += 1
                    res.append(number[j])
                    asc=1
                    break
    print(res)








def main():
    N=int(input())
    M=int(input())
    lst=list(map(int,input().split()))
    if(N==100):
        print(0)
    else:
        remote_control(N,M,lst)
    return 0


main()