import csv

def read_phonebook(filename):
    phonebook = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                phonebook.append(row)
    except FileNotFoundError:
        pass
    return phonebook

def write_phonebook(phonebook, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(phonebook)

def find_contact_by_last_name(phonebook, last_name):
    return [contact for contact in phonebook if contact[0] == last_name]

def find_contact_by_number(phonebook, number):
    return [contact for contact in phonebook if contact[2] == number]

def add_contact(phonebook, last_name, first_name, number, description):
    new_contact = [last_name, first_name, number, description]
    phonebook.append(new_contact)
    return phonebook

def update_contact_number(phonebook, last_name, new_number):
    for contact in phonebook:
        if contact[0] == last_name:
            contact[2] = new_number
            return True
    return False

def delete_contact(phonebook, last_name):
    deleted = False
    for contact in phonebook:
        if contact[0] == last_name:
            phonebook.remove(contact)
            deleted = True
            break
    return deleted

def main():
    filename = "phonebook.csv"
    phonebook = read_phonebook(filename)
    
    while True:
        print("\nВыберите действие:")
        print("1. Вывести справочник")
        print("2. Найти телефон по фамилии")
        print("3. Изменить номер телефона")
        print("4. Удалить запись")
        print("5. Найти по номеру телефона")
        print("6. Добавить запись")
        print("7. Выход")
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            for contact in phonebook:
                print(", ".join(contact))
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            found_contacts = find_contact_by_last_name(phonebook, last_name)
            if found_contacts:
                for contact in found_contacts:
                    print(", ".join(contact))
            else:
                print("Контакт не найден.")
        elif choice == '3':
            last_name = input("Введите фамилию: ")
            new_number = input("Введите новый номер телефона: ")
            if update_contact_number(phonebook, last_name, new_number):
                print("Номер успешно изменен.")
            else:
                print("Контакт не найден.")
        elif choice == '4':
            last_name = input("Введите фамилию: ")
            if delete_contact(phonebook, last_name):
                print("Контакт успешно удален.")
            else:
                print("Контакт не найден.")
        elif choice == '5':
            number = input("Введите номер телефона: ")
            found_contacts = find_contact_by_number(phonebook, number)
            if found_contacts:
                for contact in found_contacts:
                    print(", ".join(contact))
            else:
                print("Контакт не найден.")
        elif choice == '6':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            number = input("Введите номер телефона: ")
            description = input("Введите описание: ")
            phonebook = add_contact(phonebook, last_name, first_name, number, description)
            print("Контакт успешно добавлен!")
        elif choice == '7':
            write_phonebook(phonebook, filename)
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующее действие.")

if __name__ == "__main__":
    main()