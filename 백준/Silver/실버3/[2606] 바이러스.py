import sys
input = sys.stdin.readline

def DFS(graph,start):
    result,visit = [],[]
    visit.append(start)

    while (visit):
        node = visit.pop()
        if node not in result:
            result.append(node)
            visit.extend(graph[node])
            print(visit)
    return result

c=int(input())
t=int(input())
graph={}
for i in range(t):
    src,dest = map(int,input().split())
    graph[src] = graph.get(src,[])+[dest]
    graph[dest] = graph.get(dest,[])+[src]
print(graph)
ans=DFS(graph,1)
print(len(ans)-1)