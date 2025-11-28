alpha = 'abcdefghijklmnopqrstuvwxyz'
result = ['-1' for _ in range(26)]
s = input()
for i in range(len(s)):
    idx = alpha.index(s[i])
    if result[idx] == '-1':
        result[idx] = str(i) 

print(' '.join(result))