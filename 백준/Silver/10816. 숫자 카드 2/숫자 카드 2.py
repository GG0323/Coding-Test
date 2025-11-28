from collections import Counter
input(); n = list(map(int, input().split()))
input(); m = list(map(int, input().split()))
cnt = Counter(n)
print(' '.join([str(cnt[i]) for i in m]))