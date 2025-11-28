cro = ['c-','c=','dz=','d-','lj','nj','s=','z=']
word = input()
count = 0
for i in cro:
    count += word.count(i)
    
print(len(word)-count)