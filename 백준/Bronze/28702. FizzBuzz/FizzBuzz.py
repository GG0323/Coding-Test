result = 0
for _ in range(3):
    tmp = input()
    result = int(tmp) if tmp[0] in '0123456789' else result + 1
result += 1
print('FizzBuzz' if result%15 == 0 else 'Fizz' if result%3==0 else 'Buzz' if result%5 == 0 else result)