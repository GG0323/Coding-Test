from math import sqrt
for i in [input() for _ in range(int(input()))]:
    n = int(sqrt(len(i)))
    idx = n - 1
    answer = ''
    for j in range(n):
        answer += i[idx::n]
        idx -= 1
    print(answer)