import sys
input = sys.stdin.readline

def integral(lst):
    lst[0]=lst[0][:-1]
    lst=list(map(int,lst))
    print(str(lst[0]//2) + "xx+"+str(lst[1])+"x+W")

st = input().rstrip()
pl=st.split("+")
ml=st.split("-")
print(pl,ml)

