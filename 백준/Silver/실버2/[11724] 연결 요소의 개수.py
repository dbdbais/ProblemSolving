import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀를 이용시 무조건 추가

def DFS(graph,v,visited):
    visited[v]=True

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

N,M = map(int,input().split())
graph = [[]for _ in range(N+1)]
visited=[False]*(N+1)

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        DFS(graph,i,visited)
        cnt += 1

print(cnt)


