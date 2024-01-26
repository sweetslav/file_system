from choice_file import choice_number_file
from return_data_file import data_file

def copy_row():
    data, source_nf = data_file()
    count_rows = len(data)
    
    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))

        destination_nf = choice_number_file()

        if destination_nf == source_nf:
            print("Ошибка! Выбран тот же файл, в который вы хотите скопировать данные.")
            return

        with open(f'db/data_{destination_nf}.txt', 'a', encoding='utf-8') as destination_file:
            destination_file.write(data[number_row - 1])
        
        print("Данные успешно скопированы!")