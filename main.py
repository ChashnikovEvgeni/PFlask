
from asm2204.st27.models.City import City



if __name__ == '__main__':
    from group import group
else:
    from .group import group



def main():
    city = City()
    stop = False
    main_menu = [
        ["Выход", ],
        ["Показать список жителей", city.write],
        ["Добавить нового жителя", city.add],
        ["Редактировать данные жителя", city.edit_data],
        ["Удалить данные о жителе", city.delete],
        ["Удалить всю картотеку", city.full_delete],
        ["Сохранить данные о жителях в файл", city.save],
        ["Загрузить данные о жителях из файла", city.load],
    ]

    while stop == False:
        print("----------------------------------------")
        for i,menuItem in enumerate(main_menu, 1):
            print(f"[{i-1}] {menuItem[0]}")
        print("----------------------------------------")
        m = int(input("Введите номер действия: "))
        if m == 0:
            break
        else:
            try:
                main_menu[m][1]()
            except:
                print("Некорректное значение")
    group().f()



if __name__ == '__main__':
	main()


