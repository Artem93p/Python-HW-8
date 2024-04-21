# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
"""
1. Создание файла: +++
    - открываем файл на дозапись, режим a +++
2. Добавление контакта: +++
    - запросить у пользователя новый контакт +++
    - открываем файл на дозапись, режим a +++
    - добавить новый контакт +++
3. Вывод данных на экран: +++
    _ открыть файл на чтение, режим r +++
    - считать файла +++
    - вывести на экран +++
4. Поиск контакта: +++
    - выбор варианта поиска +++
    - запросить данные для поиска +++
    - окрыть файл на чтение, режим r +++
    - считываем данные файла, сохранить их в переменную  +++
    - осуществляем поиск контакта  ++++
    - выводим на экран найденный контакт +++
5. Создание UI (юзер интерфейс):
    - Вывести меню на экран +++
    - Запросить вариант денйствия у пользователя +++
    - запустить соответствующую функцию +++
    - осуществить возможносчть выхода из программы +++
"""

def input_surname():
    return input('Введите фамилию: ').title()

def input_name():
    return input('Введите имя: ').title()

def input_patronymic():
    return input('Введите отчество: ').title()

def input_phone():
    return input('Введите телефон: ')

def input_adress():
    return input('Введите город: ').title()

def create_contact():
    surname = input_surname()
    name = input_name()
    atronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    return f'{surname} {name} {atronymic} {phone} {adress} \n\n'


def add_contacts():
    contact_str = create_contact()
    with open ('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_str)

def print_contacts():
    with open ('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    #print ([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print (n, contact)


def search_contacts():
    print (
            'Возможные варианты поиска:\n'
            '1. По Фамилии\n'
            '2. По имени\n'
            '3. По отчество\n'
            '4. По номеру телефона\n'
            '5. По городу\n'
            )
    var = input( 'Выберите вариант поиска: ')
    while var not in ('1','2','3','4', '5'):
        print('Некорректный ввод')
        var = input( 'Выберите вариант поиска: ')  
    i_var = int(var) - 1
       
        
    search = input('Введите данные для поиска: ').title()
    with open ('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    #print ([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    #print (contacts_list)
    
    for str_contact in contacts_list:
        lst_contact = str_contact.split()
        if search in lst_contact [i_var]:
            print(str_contact)
    
def copy_contacts ():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        date_contacts_str = file.read()
       
    date_contacts_list = date_contacts_str.rstrip().split('\n\n')
    print()
    number_contact = int(input('введите номер контакта: '))
    print()
    for number, contacts in enumerate(date_contacts_list, 1):
        if number == number_contact:
            print (contacts)
            with open ('phonebook2.txt', 'a', encoding='utf-8') as file:
                file.write(f'{contacts} \n\n')
    print()
    print('Копирование произведено')

def interface():
    with open ('phonebook.txt', 'a', encoding='utf-8'):
        pass
    
    var = 0
    while var !='5':
        print (
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Скопировать строку в в файл phonebook2\n'
            '5. Выход'
            )
        print()
        var = input( 'Выберите вариант действия: ')
        while var not in ('1','2','3','4','5'):
            print('Некорректный ввод')
            var = input( 'Выберите вариант действия: ')
            print()
            
        match var: # Вместо if
            case '1':
                add_contacts()
            case '2' :
                print_contacts()
            case '3' :
                search_contacts()
            case '4' :
                copy_contacts()    
            case '5' :
                print('До свидания')
        print()  


if __name__== '__main__':
    interface ()
    