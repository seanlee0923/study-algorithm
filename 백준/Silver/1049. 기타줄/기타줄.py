# 입력 받기
input_split = input().split(' ')

# 줄 개수
line_num = int(input_split[0])

# 필요한 묶음 개수
total_num = int(line_num / 6)
# 묶음 사고 나머지 줄 개수
last_num = line_num % 6
brand_num = int(input_split[1])

min_total = 2147483647
min_unit = 2147483647

# 브랜드 수 만큼 총합, 개별 가격 받으면서 최소 단가 구하기
for i in range(brand_num):
    input_split = input().split(' ')
    # 필요 가격은 묶음 개수 * 묶음 개별 가격
    total_price = int(input_split[0])
    # 단가 * 줄 개수
    unit_price = int(input_split[1])
    if total_price < min_total:
        min_total = total_price
    if unit_price < min_unit:
        min_unit = unit_price

result = 0
if min_unit * 6 < min_total:
    # 따로 사는게 젤 싸면 그냥 그거로 전부 사기
    result = min_unit * line_num
else:
    # 아니면 남는 줄 개수랑 가격 비교
    result = min_total * total_num
    if last_num*min_unit > min_total:
        result = result + min_total
    else:
        result = result + last_num*min_unit

print(result)