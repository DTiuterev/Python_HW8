def write_file(data):
    with open('database.csv', 'a', encoding='utf-8') as file:
        file.writelines(data)


def read_file():
    with open('database.csv', 'r', encoding='utf-8') as file:
        return file.readlines()

