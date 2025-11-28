import sys
from queue import PriorityQueue
input = sys.stdin.readline
heap = PriorityQueue()

for i in range(int(input())):
    n = int(input())
    if n == 0:
        print('0' if heap.empty() else str(heap.get()[1]))
    else:
        heap.put((abs(n), n))