import os

CONTACTS_FILE = "contacts.txt"


def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")


def add_contact():
    name = input("Введите имя: ").strip()
    phone = input("Введите телефон: ").strip()
    email = input("Введите email: ").strip()
    
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Контакт добавлен!")


def search_contact():
    query = input("Введите имя или телефон для поиска: ").strip().lower()
    contacts = load_contacts()
    
    found_contacts = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    
    if found_contacts:
        print("\nНайденные контакты:")
        for c in found_contacts:
            print(f"Имя: {c['name']}, Телефон: {c['phone']}, Email: {c['email']}")
    else:
        print("Контакт не найден.")


def delete_contact():
    name = input("Введите имя контакта для удаления: ").strip().lower()
    contacts = load_contacts()
    
    new_contacts = [c for c in contacts if c["name"].lower() != name]
    
    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print("Контакт удалён!")
    else:
        print("Контакт не найден.")


def update_contact():
    name = input("Введите имя контакта, который нужно обновить: ").strip().lower()
    contacts = load_contacts()
    
    for contact in contacts:
        if contact["name"].lower() == name:
            print("Введите новые данные (оставьте поле пустым, если не хотите изменять):")
            new_name = input(f"Новое имя ({contact['name']}): ").strip() or contact["name"]
            new_phone = input(f"Новый телефон ({contact['phone']}): ").strip() or contact["phone"]
            new_email = input(f"Новый email ({contact['email']}): ").strip() or contact["email"]
            
            contact["name"], contact["phone"], contact["email"] = new_name, new_phone, new_email
            save_contacts(contacts)
            print("Контакт обновлён!")
            return
    
    print("Контакт не найден.")


def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\nСписок контактов:")
        for c in contacts:
            print(f"Имя: {c['name']}, Телефон: {c['phone']}, Email: {c['email']}")
    else:
        print("Список контактов пуст.")


def main():
    while True:
        print("\nУправление контактами:")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Удалить контакт")
        print("4. Обновить контакт")
        print("5. Показать все контакты")
        print("6. Выйти")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
