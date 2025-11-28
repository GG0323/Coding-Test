arr = [input() for i in range(5)]
max_l = len(max(arr, key=lambda x : len(x)))
print(''.join([arr[j][i] if len(arr[j]) > i else '' for i in range(max_l) for j in range(5)]))