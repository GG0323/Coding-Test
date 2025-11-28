import  sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    word = input()
    lst = word[0]
    for i in range(1, len(word)):
        if word[i] != word[i-1] and word[i] in lst:
            lst = ''
            break
        lst += word[i]
    count += 1 if lst else 0

print(count)