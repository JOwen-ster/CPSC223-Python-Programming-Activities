# Owen Sterling
# 8/31/2023
# Python program that performs as a Tuffy Titan Contact List
#which contains a list of contacts that can be modified or deleted.

def print_list(list):
    print("================== CONTACT LIST ==================\nIndex   First Name            Last Name\n======  ====================  ====================")
    index = 0
    for i in list:
        print(f'{str(index):8}{list[index][0]:22}{list[index][1]:22}')
        index+=1
    
def add_contact(list):
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    list.append([first,last])
    return list

def modify_contact(list):
    index = int(input("Enter the index number: "))
    if(index > (len(list) - 1)):
        print("Invalid index number.")
        return list # myb print and return the msg not just print the msg and return the list

    first = input("Enter first name: ")
    last = input("Enter last name: ")
    list[index] = [first,last]
    return list

def delete_contact(list):
    index = int(input("Enter the index number: "))
    if(index > (len(list) - 1)):
        print("Invalid index number.")
        return list # myb print and return the msg not just print the msg and return the list
    
    list.pop(index)
    return list