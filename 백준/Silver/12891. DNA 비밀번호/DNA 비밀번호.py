s, p = map(int, input().split())
dna = input(); wnt = list(map(int, input().split()))
check = [0] * 4
dic = {k:i for i, k in enumerate('ACGT')}

for i in dna[:p]:
    check[dic[i]] += 1

answer = 1 if [1 if check[i] - wnt[i] > -1 else 0 for i in range(4)].count(0) == 0 else 0

for i in range(s-p):
    check[dic[dna[i]]] -= 1
    check[dic[dna[p+i]]] += 1
    if all(check[j] >= wnt[j] for j in range(4)):
        answer += 1
print(answer)