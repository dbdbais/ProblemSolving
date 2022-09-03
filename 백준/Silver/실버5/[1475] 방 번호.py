import sys
input = sys.stdin.readline
digit=[0]*10
st=input().rstrip()
for i in range(len(st)):
    digit[int(st[i])] += 1
six_nine=digit[6]+digit[9]
digit[6] = 0
digit[9] = 0
if(six_nine%2 == 1):
    six_nine = (six_nine // 2) + 1
else:
    six_nine = six_nine // 2
print(max(max(digit),six_nine))
