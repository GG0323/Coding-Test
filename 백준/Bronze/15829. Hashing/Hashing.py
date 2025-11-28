dic = {key:val+1 for val,key in enumerate('abcdefghijklmnopqrstuvwxyz')}
r = [31 ** i for i in range(int(input()))]
l = input()
result = sum([r[idx] * dic[i] for idx, i in enumerate(l)])
print(result % 1234567891)