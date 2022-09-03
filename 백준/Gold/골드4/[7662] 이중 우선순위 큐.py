import heapq
import sys
input = sys.stdin.readline

T=int(input())
for i in range(T):
    max_heap,min_heap= [],[]
    visit= [False]*1000001
    q=int(input())
    for j in range(q):
        order,num = input().split()

        if (order == "I"):
            heapq.heappush(min_heap,(int(num),j))
            heapq.heappush(max_heap,(-int(num),j))
            visit[j] = True
        else:
            if (int(num) == -1):
                while (min_heap and not visit[min_heap[0][1]]):
                    heapq.heappop(min_heap)
                if (min_heap):
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif (int(num) == 1):
                while (max_heap and not visit[max_heap[0][1]]):
                    heapq.heappop(max_heap)
                if(max_heap):
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while (min_heap and not visit[min_heap[0][1]]):
        heapq.heappop(min_heap)
    while (max_heap and not visit[max_heap[0][1]]):
        heapq.heappop(max_heap)

    if(len(min_heap) and len(max_heap)):

        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")






