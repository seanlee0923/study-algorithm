N = int(input())
a = fibo = 0
b = 1

for i in range(1, N):
    fibo = a+b
    a = b
    b = fibo

print(b)
