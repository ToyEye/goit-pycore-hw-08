from handlers import add_contact,remove_phone,find_phone, change_contact, show_all,show_phone,delete_contact, add_birthday,show_birthday,birthdays

from classes import AddressBook


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

   

def main():

    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command =='change':
            print(change_contact(args,book))
        elif command == "phone":
            print(show_phone(args,book))
        elif command == "find-phone":
            print(find_phone(args,book))         
        elif command == "all":
            for result in show_all(book):
                print(result)
        elif command == "remove":
            print(remove_phone(args,book))           
        elif command == "add-birthday":
            print(add_birthday(args,book))
        elif command == "show-birthday":
            print(show_birthday(args,book))
        elif command == "delete":
            print(delete_contact(args,book))
        elif command == "birthdays":
            for result in birthdays(book):
                print(result)                

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()