st=input()
st=st.upper()
res=0
count=0
suc=-1
alp=[]
for i in range(26):
        res=st.count(chr((ord('A')+i)))
        alp.append(res)
for i in range(26):
    if(alp[i]==max(alp)):
        count=count+1
        if(count>1):
            suc=-1
            break
        suc=i
if(suc==-1):
    print("?")
else:
    print(chr((ord('A')+suc)))
