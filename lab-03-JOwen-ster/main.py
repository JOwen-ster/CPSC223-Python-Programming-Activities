# Owen Sterling
# 8/31/2023
# Python program that performs as a Tuffy Titan Contact List
#which contains a list of contacts that can be modified or deleted.
# """
# """ is a multiline string
from contacts import *
contactList = [] # ['Richard', 'Stallman'],['Bill', 'Gates'],['Steve', 'Jobs']
def runner():
    while(True):
        print("      *** TUFFY TITAN CONTACT MAIN MENU\n")
        print("1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Sort list by first name")
        print("6. Sort list by last name")
        print("7. Exit the program")
        print()
        choice = int(input("Enter the menu choice: "))
        print()
        match choice:
            case 1:
                print_list(contactList)
            case 2:
                first_name = first()
                last_name = last()
                add_contact(contactList, first_name=first_name, last_name=last_name)
            case 3:
                index = int(input("Enter the index number: "))
                first_name = first()
                last_name = last()
                done = modify_contact(contactList, first_name=first_name, last_name=last_name, index=index)
                if not done:
                    print("Invalid index number.")
            case 4:
                index = int(input("Enter the index number: "))
                done = delete_contact(contactList, index=index)
                if not done:
                    print("Invalid index number.")
            case 5:
                sort_contacts(contactList, column = 0)
            case 6:
                sort_contacts(contactList, column = 1)
            case 7:
                exit(0)
            case _:
                exit(1)
        print()
runner()