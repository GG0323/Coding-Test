k = input()
if len(k) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    tmp = int(k[1]) - int(k[0])
    flag = True
    for i in range(1, len(k)):
        if int(k[i]) - int(k[i-1]) != tmp:
            flag = False
            break
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!' if flag else '흥칫뿡!! <(￣ ﹌ ￣)>')