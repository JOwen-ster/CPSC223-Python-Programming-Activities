# Owen Sterling
# 9/28/2023
# Python program that executes Contact List Commands
import contacts


# 1. Create a `main` driver program to meet the following requirements:
#      1. Create a file named `main.py`.
#      1. Add a comment at the top of the file which indicates your name, date and the purpose of the file.
#      1. Import the `contacts` module.
#      2. Define a variable to use for the contact dictionary. 
#      3. Implement a menu within a loop with following choices:
#           1. Add contact
#           1. Modify contact
#           1. Delete contact
#           1. Print contact list (sorted)
#           1. Find contact
#           1. Exit the program
#      4. Prompt the user for the menu choice.
#      5. Prompt the user for the information needed for the appropriate `contacts` function and call the function.
#      6. Print out appropriate errors with function return values of `error`.
contact:dict={}

def first():
    first = input("First Name")
    return first

def last():
    last = input("Last Name")
    return last

def id():
    id = input("Id")
    return id

def runner():
    while(True):
        print('      *** TUFFY TITAN CONTACT MAIN MENU')
        print()
        print("1. Add contact")
        print("2. Modify contact")
        print("3. Delete contact")
        print("4. Print contact list (sorted)")
        print("5. Find contact")
        print("6. Exit the program")
        print()
        choice = int(input("Enter the menu choice: "))
        print()
        match choice:
            case 1:
                id_ = id()
                first_name = first()
                last_name = last()
                print(contacts.add_contact(contact, id=id_, first_name=first_name, last_name=last_name))
            case 2:
                id_ = id()
                first_name = first()
                last_name = last()
                print(contacts.modify_contact(contact, id=id_, first_name=first_name, last_name=last_name))
            case 3:
                id_ = id()
                print(contacts.delete_contact(contact, id_))
            case 4:
                contacts.print_list(contact)
            case 5:
                find_ = input('Find')
                print(contacts.find_contact(contact, find=find_))
            case 6:
                exit(0)
            case _:
                exit(1)
        print()
runner()

