input()
score = list(map(int, input().split()))
print(f'{sum(score)*100/max(score)/len(score)}')