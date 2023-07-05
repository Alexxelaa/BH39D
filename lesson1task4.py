#номер 4
num1 = input()
num2 = input()
num3 = input()
list = [num1, num2, num3]
length = len(list)
negative = length - num1.isdigit() - num2.isdigit() - num3.isdigit()
positive = num1.isdigit() + num2.isdigit() + num3.isdigit()
print(f"отрицательных чисел: {negative}")
print(f"положительных чисел / ноль:  {positive}")
