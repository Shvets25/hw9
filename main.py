def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please try again."

    return wrapper

class ContactBook:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Added {name} with phone {phone} to contacts."

    @input_error
    def change_phone(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            return f"Changed phone for {name} to {new_phone}."
        else:
            return f"{name} not found in contacts."

    @input_error
    def get_phone(self, name):
        if name in self.contacts:
            return f"The phone number for {name} is {self.contacts[name]}."
        else:
            return f"{name} not found in contacts."

    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts found."
        else:
            result = "Contacts:\n"
            for name, phone in self.contacts.items():
                result += f"{name}: {phone}\n"
            return result

def main():
    contact_book = ContactBook()
    while True:
        command = input("Enter a command: ").strip().lower()
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split(" ", 2)
            response = contact_book.add_contact(name, phone)
            print(response)
        elif command.startswith("change"):
            _, name, new_phone = command.split(" ", 2)
            response = contact_book.change_phone(name, new_phone)
            print(response)
        elif command.startswith("phone"):
            _, name = command.split(" ", 1)
            response = contact_book.get_phone(name)
            print(response)
        elif command == "show all":
            response = contact_book.show_all_contacts()
            print(response)
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
