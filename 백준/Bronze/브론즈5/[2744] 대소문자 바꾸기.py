import sys
input = sys.stdin.readline

st=input().rstrip()
for i in st:
    if(i.isupper()):
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")
