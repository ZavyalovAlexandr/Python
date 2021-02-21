my_list = []
for idx in range(1, 1000, 2):
    my_list.append(idx**3)
print('список, состоящий из кубов нечётных чисел от 0 до 1000: ', my_list)

sum_division_by_7 = 0
for number in my_list:
    number = str(number)
    sum_figures = 0
    for figure in number:
        sum_figures = sum_figures + int(figure)
    if sum_figures % 7 == 0:
        sum_division_by_7 = sum_division_by_7 + sum_figures

print('Сумма чисел из списка, сумма цифр которых делится нацело на 7 =',
      sum_division_by_7)

sum_division_by_7 = 0
for number in my_list:
    number = str(number+17)
    sum_figures = 0
    for figure in number:
        sum_figures = sum_figures + int(figure)
    if sum_figures % 7 == 0:
        sum_division_by_7 = sum_division_by_7 + sum_figures

print('Сумма чисел из списка, сумма цифр которых, после прибавления 17 делится нацело на 7 =',
      sum_division_by_7)
