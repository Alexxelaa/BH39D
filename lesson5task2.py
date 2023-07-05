k = int(input()) #начальное число
m = int(input()) #числа кратные m
n = int(input()) #количество чисел
start = 0
while start < n:
    if k % m == 0:
        print(k)
        start += 1
    k += 1
