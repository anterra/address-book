# prompt: create your own command-line address-book program using which you can
# browse, add, modify, delete or search for your contacts such as friends, family and colleagues
# and their information such as email address and/or phone number.
# details must be stored for later retrieval.

# planning:
# class Contact will define a person and their contact information
# different methods to view all, search for, add, delete, modify contacts
# program should ask you what you want to do, at beginning, when viewing all, and when viewing a specific contact
# storage for later retrieval indicates use of pickle

# work flow notes:

# ver 1: address_book as a list of contacts (being Contact objects). name of object was person's name,
#   but was separate from their actual name, which would make it difficult to create new contacts --
#   would have to define both name of person object and name of person.. needed rethinking
# ver 2: use dictionary instead. that way name is key and can be more easily accessed and manipulated
# ver 3: got dictionary of contacts to work, by storing multiple details as a list, then the list is the ssingle value
#   for the name key. implemented pickle and storage of contacts
# ver 4: added "group" classification to contacts so they could be sorted by type of contact
# ver 5: all functionality is working and thoroughly tested! only problem: changes made to address_book (new or deleted
#   contacts) don't save/load on subsequent runs of the program. (i.e. running again resets to default contacts)...
#   also needs modify method
# ver 6: added modify method. plan to get modifications to store: keep the address_book.data file somewhere else on the
#   hard drive and refer to that path so changes are kept and called on each retrieval.
#   also: if a contact name key doesn't exist when searched for, need to print a "no such contact" response -- but only
#   once! right now its printing as many times as there are contacts who are not the specified key since its in a for
#   loop, even if the key does exist
# ver 7: fixed above issue with else: no key statement, by switching from iterating over dict indexes, to instead using
#   dict.get() method, which allows me to provide a failure message if no key found.
# ver 8: instead of iterating over (names, detail) in stored_contacts.items(), replaced with dictionary methods
#   .keys(), .values(), .get()

# NOTE: I realize this is not object oriented, but rather functional programming
# load contacts functions? since i reload from pickle so many times might as well enclose it in a function if reused


import pickle

class Contact:
    def __init__(self, name, number, email, group):
        self.name = name
        self.number = number
        self.email = email
        self.group = group


# default list of contacts
Liz = Contact("Liz", "402.7297", "liz@gmail.com", "friends")
Devon = Contact("Devon", "461.9025", "devon@gmail.com", "friends")
Dad = Contact("Dad", "301.0250", "dad@gmail.com", "family")
Hope = Contact("Hope", "620.0863", "hope@gmail.com", "family")
James = Contact("James", "208.3246", "james@gmail.com", "colleagues")
Laura = Contact("Laura", "516.0275", "laura@gmail.com", "colleagues")


address_book_file = "address_book.data"
address_book = {
    Liz.name: [Liz.number, Liz.email, Liz.group],
    Devon.name: [Devon.number, Devon.email, Devon.group],
    Dad.name: [Dad.number, Dad.email, Dad.group],
    Hope.name: [Hope.number, Hope.email, Hope.group],
    James.name: [James.number, James.email, James.group],
    Laura.name: [Laura.number, Laura.email, Laura.group]
}


f = open(address_book_file, "wb")
pickle.dump(address_book, f)
f.close()
del address_book


def browse():
    """Allows the user to view all the names in the address book"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    print("\nContacts in Address Book:")
    for names, details in stored_contacts.items():
        print(names)
    print("\n")


def view():
    """Allows the user to view all contact details of a contact"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    person = input("Who's contact details would you like to view? ")
    details = stored_contacts.get(person, "No such contact")
    if details != "No such contact":
        print("\nName: {}, Number: {}, Email: {}\n".format(person, details[0], details[1]))
    else:
        print(details)


def search():
    """Allows the user to search the address book for a certain person or group of people"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    type = input("Are you searching for a person or a group? ")
    if type == "person":
        person = input("Who are you searching for? ")
        for names, details in stored_contacts.items():
            if person == names:
                proceed = input("Found contact {}. Would you like to view their contact information? ".format(person))
                if proceed == "yes":
                    print("Name: {}, Number: {}, Email: {}".format(names, details[0], details[1]))
            else:
                proceed = input("No contact {} exists. Would you like to create a new contact?".format(person))
                if proceed == "yes":
                    add()
                    break
                else:
                    break
    elif type == "group":
        group = input("Which group would you like to view? [friends], [family], or [colleagues]: ")
        print("\nThe contacts in group '{}' are: ".format(group))
        for names, details in stored_contacts.items():
            if group == details[2]:
                print(names)
        print("\n")


def add():
    """Allows the user to add someone new to the address book"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    newcontact_name = input("What is the name of the contact you would like to add? ")
    newcontact_number = input("What is their number? ")
    newcontact_email = input("What is their email address? ")
    newcontact_group = input("What group are they in? [friends] [family] [colleagues] ")

    stored_contacts[newcontact_name] = [newcontact_number, newcontact_email, newcontact_group]
    f = open(address_book_file, "wb")
    pickle.dump(stored_contacts, f)
    f.close()
    print("\nNew contact {} has been created.\n".format(newcontact_name))


def delete():
    """Allows the user to delete a contact from the address book"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    contact = input("Who would you like to delete? ")
    del stored_contacts[contact]
    f = open(address_book_file, "wb")
    pickle.dump(stored_contacts, f)
    f.close()
    print("\n{} has been deleted.\n".format(contact))


def modify():
    """Allows the user to modify a contact's details"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    contact = input("Which contact would you like to modify? ")
    for names, details in stored_contacts.items():
        if contact in names:
            info_type = input("What info would you like to change? [number] [email] [group] ")
            if info_type == "number":
                variable = 0
            elif info_type == "email":
                variable = 1
            elif info_type == "group":
                variable = 2
            else:
                print("invalid entry")
                break
            info = input("What is their new {}? ".format(info_type))
            f = open(address_book_file, "wb")
            details[variable] = info
            pickle.dump(stored_contacts, f)
            f.close()
            print("{}'s {} has been updated to {}.".format(contact, info_type, info))


while True:
    action = input("""What would you like to do?: 
            [browse] address book
            [view] a contact's details
            [modify] a contact's details
            [search] for a person or group of people
            [add] someone new
            [delete] someone
            [quit] --> """)
    if action == "quit":
        break
    elif action == "browse":
        browse()
    elif action == "view":
        view()
    elif action == "search":
        search()
    elif action == "delete":
        delete()
    elif action == "add":
        add()
    elif action == "modify":
        modify()
    else:
        print("Unknown action\n")
