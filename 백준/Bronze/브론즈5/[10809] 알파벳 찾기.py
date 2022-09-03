S=input()
for i in range(26):
    tmp=S.find(chr(ord('a')+i))
    print(tmp,end=" ")
