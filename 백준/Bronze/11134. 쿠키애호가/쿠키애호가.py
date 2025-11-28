for _ in range(int(input())):
    n, c = map(int, input().split())
    print(n//c + int(bool(n%c!=0)))