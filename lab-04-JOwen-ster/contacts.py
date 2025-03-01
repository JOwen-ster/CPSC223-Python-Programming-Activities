# Owen Sterling
# 9/14/2023
# Python program that performs as a Tuffy Titan Contact List
#which contains a list of contacts that can be modified or deleted.

def print_list(contact):
    '''
    Prints the list
    '''
    print('==================== CONTACT LIST ====================')
    print('Last Name             First Name             Phone    ')
    print('==================  =======================  =========')
    index = 0
    for key,value in (sort_contacts(contact)).items():
        print(f'{str(value[1]):20}{str(value[0]):25}{key}')
        index+=1

def add_contact(contact:dict, /, *, id, first_name, last_name) -> any:
    '''
    Adds a contact to the list
    '''
    if id in contact.keys():
        return F'error'
    
    new_contact = {id:[first_name, last_name]}
    contact.update(new_contact)
    return new_contact

def modify_contact(contact:dict, /, *, id, first_name, last_name):
    '''
    Sets a contact to the specified values
    '''
    if id not in contact.keys():
        return F'error'
    
    new_contact = {id:[first_name, last_name]}
    contact[id] = [first_name, last_name]
    return new_contact

def delete_contact(contact:dict, /, *, id):
    '''
    Delete a contact
    '''
    if id not in contact.keys():
        return F'error'

    popped_pair_value = contact.pop(id)
    popped_pair = {id:popped_pair_value}
    return popped_pair


def sort_contacts(contact: dict):
    '''
    Sorts the list by last or first name
    '''
    contacts = dict(sorted(contact.items(), key = lambda x: (x[1][0], x[1][1])))
    return contacts

def find_contact(contact: dict, find: str=None):
    '''
    Finds a contact
    '''
    new_contacts = {}
    if find.isdigit() and int(find) in contact.keys():
        found = {int(find) : [contact[int(find)][0], contact[int(find)][1]]}
        new_contacts.update(found)
    else:
        for key,value in contact.items():
            if (find.lower() in value[0].lower()) or (find.lower() in value[1].lower()):
                new_contacts.update({key:value})
        new_contacts = sort_contacts(new_contacts)
    return new_contacts
