# prompt: create your own command-line address-book program using which you can
# browse, add, modify, delete or search for your contacts such as friends, family and colleagues
# and their information such as email address and/or phone number.
# details must be stored for later retrieval.

# planning:
# class Contact will define a person and their contact information
# different methods to view all, search for, add, delete, modify contacts
# program should ask you what you want to do, at beginning, when viewing all, and when viewing a specific contact

# work flow notes:

# ver 1: stored for later retrieval indicates pickle method. list of contacts. name of object was person's name,
#   but was separate from their actual name, which would make it difficult to create new contacts --
#   would have to define both name of person object and name of person
# ver 2: use dictionary instead. that way name is key and can be more easily accessed and manipulated


import pickle


class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email


# default list of contacts
Liz = Contact("Liz", "402.7297", "liz@gmail.com")
Devon = Contact("Devon", "461.9025", "devon@gmail.com")
Dad = Contact("Dad", "301.0250", "dad@gmail.com")
Hope = Contact("Hope", "620.0863", "hope@gmail.com")
James = Contact("James", "208.3246", "james@gmail.com")
Laura = Contact("Laura", "516.0275", "laura@gmail.com")


address_book_file = "address_book.data"
address_book = {
    Liz.name: [Liz.number, Liz.email],
    Devon.name: [Devon.number, Devon.email],
    Dad.name: [Dad.number, Dad.email],
    Hope.name: [Hope.number, Hope.email],
    James.name: [James.number, James.email],
    Laura.name: [Laura.number, Laura.email]
}

f = open(address_book_file, "wb")
pickle.dump(address_book, f)
f.close()
del address_book


def browse():
    """Allows the user to view the entire address book"""
    # returns a list of names
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    print("Contacts in Address Book:")
    for names, details in stored_contacts.items():
        print(names)


def view():
    """Allows the user to view all contact details of a contact"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    person = input("Who's contact details would you like to view? ")
    for names, details in stored_contacts.items():
        if person in names:
            print("Name: {}, Number: {}, Email: {}".format(names, details[0], details[1]))
            break
        else:
            print("No contact {} exists.".format(person))


def search():
    """Allows the user to search the address book for a certain person or group of people"""
    person = input("Who are you searching for? ")
    for contacts in address_book:
        if contact == contacts.name:
            proceed = input("Found contact {}. Would you like to view their contact information? ".format(contact))
            if proceed == "yes":
                view()
            else:
                break


def add(contact):
    """Allows the user to add someone to the address book"""

    # print("{} has been added.".format(newcontact.name))


def delete(contact):
    """Allows the user to delete a contact"""


while True:
    contact = Contact("", "", "")
    action = input("""What would you like to do?: 
            [browse] address book
            [view] a contact
            [search] for someone
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
        contact = input("Who would you like to delete? ")
        del address_book[contact]
    elif action == "add":
        add()
    else:
        print("Unknown action")
