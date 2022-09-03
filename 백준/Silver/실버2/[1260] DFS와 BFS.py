from collections import deque

def dfs(graph,start):
    visited=[]
    stack=deque()

    stack.append(start)

    while (stack):
        node=stack.pop()

        if node not in visited:
            visited.append(node)
            tmp = list(graph[node])
            tmp.sort(reverse=True)
            for i in tmp:
                stack.append(i)
    for i in visited:
        print(i,end=" ")


def bfs(graph, start):
    visited = []
    queue = deque()

    queue.append(start)

    while (queue):
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            tmp = list(graph[node])
            tmp.sort()
            for i in tmp:
                queue.append(i)
    for i in visited:
        print(i, end=" ")


N,M,V = map(int,input().split())
graph={}
for n in range(1,N+1):
    graph[n] = []
for i in range(M):
    src,dest = map(int,input().split())
    graph[src] = graph.get(src, []) + [dest]
    graph[dest] = graph.get(dest, []) + [src]
dfs(graph,V)
print()
bfs(graph,V)
