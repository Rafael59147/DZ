first_field = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('Первое поле: ', first_field)
def code(numbers):
    password = []
    for i in range(1, numbers + 1):
        for j in range(i + 1, numbers + 1):
            sum_ = i + j
            if numbers % sum_ == 0:
                password.append(i)
                password.append(j)
    return password


numbers = int(input('Введите число из первого поля:'))
password = code(numbers)
print(*password, sep='')
