def sort_data(number, read, write, sor, dat, data):
    while True:
        n = number()
        if n == '1':
            print(*read(), sep='')
        elif n == '2':
            print(*sor(input('Введите id ученика: '), read()), sep='')
        elif n == '3':
            print(*sor(input('Введите фамилию ученика: '), read()), sep='')
        elif n == '4':
            print(*sor(input('Введите № класса: '), read()), sep='')
        elif n == '5':
            write(data())
        elif n == '6':
            print('Работа с базой данных завершена по вашему запросу ')
        break