import sys
sys.stdin.readline

input(); a = set(map(int, input().split()))
m = int(input()); lst = list(map(int, input().split()))
result = set(lst) - a

for i in lst:
    print(int(i not in result))