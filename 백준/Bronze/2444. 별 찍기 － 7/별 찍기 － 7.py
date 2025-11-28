star = ['*']
emp = ' '
num = int(input())
for i in range(1, num*2):
    if i < num:
        print(f'{emp*(num-i)}{star[i-1]}')
        star.append(star[i-1]+'**')
    else:
        print(f'{emp*(i-num)}{star[num-i-1]}')