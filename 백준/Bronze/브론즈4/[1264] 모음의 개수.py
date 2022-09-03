while (True):
    count = 0
    st=input()
    if(st=="#"):
        break
    st=st.lower()
    for a in st:
        if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
            count += 1
    print(count)
