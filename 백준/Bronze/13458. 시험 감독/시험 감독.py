result = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

for i in a:
    i -= b
    if i > 0:
        result += i // c + int(bool(i % c))

print(result)