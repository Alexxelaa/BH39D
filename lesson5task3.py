n = int(input())
l = list(range(2, n+1, 2))
str_l = list(map(str, l))
for i in range(0, len(l), 5):
    print(' '.join(str_l[i:i+5]))
