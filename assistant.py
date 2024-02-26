
import handlers
from classes import AddressBook
import data

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

   

def main():

    book = data.load_data()
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
            print(handlers.add_contact(args, book))
        elif command =='change':
            print(handlers.change_contact(args,book))
        elif command == "phone":
            print(handlers.show_phone(args,book))
        elif command == "find-phone":
            print(handlers.find_phone(args,book))         
        elif command == "all":
            for result in handlers.show_all(book):
                print(result)
        elif command == "remove":
            print(handlers.remove_phone(args,book))           
        elif command == "add-birthday":
            print(handlers.add_birthday(args,book))
        elif command == "show-birthday":
            print(handlers.show_birthday(args,book))
        elif command == "delete":
            print(handlers.delete_contact(args,book))
        elif command == "birthdays":
            for result in handlers.birthdays(book):
                print(result)                

        else:
            print("Invalid command.")
    data.save_data(book)        

if __name__ == "__main__":
    main()