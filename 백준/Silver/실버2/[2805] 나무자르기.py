import sys
input=sys.stdin.readline
N,M = map(int,input().split())
tree = list(map(int,input().split()))
start, end= 1,max(tree)
tree_sum=0
while (start <= end):
    mid= (start+end)//2

    for i in range(N):
        if(tree[i]>=mid):
            tree_sum = tree_sum + (tree[i]-mid)
    if(tree_sum>=M):
        start = mid+1
    else:
        end= mid-1
    tree_sum = 0
print(end)