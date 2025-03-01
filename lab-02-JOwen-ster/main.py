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
        print("5. Exit the program")
        print()
        choice = int(input("Enter the menu choice: "))
        print()
        match choice:
            case 1:
                print_list(contactList)
            case 2:
                add_contact(contactList)
            case 3:
                modify_contact(contactList)
            case 4:
                delete_contact(contactList)
            case 5:
                exit(0)
            case _:
                exit(1)
        print()

runner()
