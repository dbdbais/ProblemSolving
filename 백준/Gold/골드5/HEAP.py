import heapq
import sys
input = sys.stdin.readline

heap= [7,2,4,3,1]
heap=[-x for x in heap]
heapq.heapify(heap)

print(heap)