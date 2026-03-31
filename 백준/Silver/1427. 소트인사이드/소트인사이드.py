num = int(input())

# 일단 자릿수를 구하자
cnt = 0
a = 10
i = 1

while num > i:
    cnt += 1
    i *= 10

int_arr=[]
# 자릿수만큼 반복하자
for j in range(1, cnt):
    dev_num = 10**(cnt-j)
    int_arr.append(num//dev_num)
    num = num%dev_num
int_arr.append(num)
int_arr.sort(reverse=True)
print(*int_arr,sep='')