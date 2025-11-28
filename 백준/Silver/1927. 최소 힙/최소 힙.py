import sys
from queue import PriorityQueue
input = sys.stdin.readline
heap = PriorityQueue()

for i in range(int(input())):
    n = int(input())
    if n == 0:
        print('0' if heap.empty() else heap.get())
    else:
        heap.put(n)