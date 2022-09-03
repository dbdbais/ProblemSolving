import sys
input = sys.stdin.readline

A,B= map(int,input().split())
ast=set(map(int,input().split()))
bst=set(map(int,input().split()))

print(len(bst-ast)+len(ast-bst))

