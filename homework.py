sum_n = 0
count = 0
min_a = 0
max_a = 0
even = 0
noeven = 0
while True:
    a = int(input('Введите числа:'))
    if a == 0:
        break
    else:
        count += 1
        sum_n += a
    if a < min_a:
        min_a += a
    if a > max_a:
        max_a = a
    if int(a) % 2 == 0:
        even += 1
    else:
        noeven += 1
print('количество: ', count)
print('сумма: ', sum_n)
print('среднее значение:', sum_n / count)
print('минимальное и максимальное числа', min_a, max_a)
print('четных', even, 'не четных', noeven)

















