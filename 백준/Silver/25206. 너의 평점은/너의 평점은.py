dic = {'A+':4.5, 'A0':4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5,
       'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
result = [0, 0]  # 총 학점, 과목별 학점*평점 합

for _ in range(20):
    score = input().split()
    if score[-1] == 'P':
        continue
    result[0] += float(score[1])
    result[1] += dic[score[2]] * float(score[1])

print(f'{result[1]/result[0]:4f}')