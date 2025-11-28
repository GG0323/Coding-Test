import sys
from queue import PriorityQueue
input = sys.stdin.readline
heap = PriorityQueue()
arr = [int(input()) for _ in range(int(input()))]
Max = max(arr)

for i in arr:
    if i == 0:
        print('0' if heap.empty() else heap.get()[1])
    else:
        heap.put((Max-i, i))