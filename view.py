def get_data():
    return f"{input('Введите id: ')} {input('Введите фамилию: ')} {input('Введите имя: ')} {input('Введите класс: ')}\n"


def get_action():
    return input('Введите номер действия с базой данных учеников школы:\n \
        где: 1 - показать всю базу данных\n \
             2 - показать информацию об ученике по его id\n \
             3 - показать информацию об ученике по его фамилии\n \
             4 - показать информацию об учениках выбранного класса\n \
             5 - добавить ученика\n \
             6 - завершить работу\n ')

