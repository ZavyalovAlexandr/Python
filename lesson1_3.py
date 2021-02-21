names = ['ов', '', 'а', 'а', 'а', 'ов', 'ов',
         'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов',
         'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов']
user_percent = 0
for idx in names:
    print(user_percent, 'процент' + idx)
    user_percent += 1

# вариант 2
print('вариант 2')
names2 = ['ов', '', 'а', 'а', 'а']
for idx in range(0, 101):
    if idx%100 > 10 and idx%100 < 15:
        print(idx, 'процент' + names2[0])
    elif idx%10 > 4:
        print(idx,'процент' + names2[0])
    else:
        print(idx, 'процент' + names2[idx % 10])
