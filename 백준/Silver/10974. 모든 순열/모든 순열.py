num = int(input())

def back(n, lev):
    if lev == num:
        print(n.rstrip())
        return
    
    for i in range(1, num+1):
        if str(i) in n:
            continue
        back(n+str(i)+' ', lev+1)

back('', 0)