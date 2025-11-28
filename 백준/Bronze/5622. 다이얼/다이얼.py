dic = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
word = input()
print(sum([v if i in k else 0 for k, v in dic.items() for i in word]))