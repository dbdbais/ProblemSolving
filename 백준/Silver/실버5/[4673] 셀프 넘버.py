import sys
input = sys.stdin.readline

natural_num = set(range(1,10001))
gen_num = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    gen_num.add(i)
self_num = sorted(natural_num-gen_num)
for i in self_num:
    print(i)