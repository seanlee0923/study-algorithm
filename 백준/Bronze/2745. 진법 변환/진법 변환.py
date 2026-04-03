# 입력을 받자
input_split = input().split(' ')
N = input_split[0]
B = input_split[1]
result = 0

# 문자열 순회
for i in range (len(N)):
    # 0부터 시작하니까 1 더 뺴기
    unit_char = N[len(N)-i-1]
    unit_num = 0
    if unit_char.isdigit():
        unit_num = int(unit_char)
    else:
        unit_num = ord(unit_char)-55
        # 이런 제곱도 되네
    calc_num = int(B)**i
    result += unit_num * calc_num

print(result)