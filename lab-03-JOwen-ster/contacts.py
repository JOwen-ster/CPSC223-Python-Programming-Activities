# Owen Sterling
# 9/14/2023
# Python program that performs as a Tuffy Titan Contact List
#which contains a list of contacts that can be modified or deleted.

def print_list(list):
    '''
    Prints the list
    '''
    print("================== CONTACT LIST ==================\nIndex   First Name            Last Name\n======  ====================  ====================")
    index = 0
    for i in list:
        print(f'{str(index):8}{list[index][0]:22}{list[index][1]:22}')
        index+=1
    
def add_contact(list, first_name="", last_name=""):
    '''
    Adds a contact to the list
    '''
    list.append([first_name,last_name])

def modify_contact(list, first_name="", last_name="", index=0):
    '''
    Sets a contact to the specified values
    '''
    if(index > (len(list) - 1)):
        print("Invalid index number.")
        return False

    list[index] = [first_name,last_name]
    return True

def delete_contact(list, index=0):
    '''
    Delete a contact at an index
    '''
    if(index > (len(list) - 1)):
        print("Invalid index number.")
        return False
    
    list.pop(index)
    return list

def sort_contacts(contact_list_, column=0):
    '''
    Sorts the list by last or first name
    '''
    if column < 0 or column > 1:
        return False
    contact_list_.sort(key = lambda x: x[column])
    return True

def first():
    first_name = input("Enter first name: ")
    return first_name

def last():
    last_name = input("Enter last name: ")
    return last_name

def name():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    return first_name ,last_name