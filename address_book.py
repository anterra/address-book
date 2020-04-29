# prompt: create your own command-line address-book program using which you can
# browse, add, modify, delete or search for your contacts such as friends, family and colleagues
# and their information such as email address and/or phone number.
# details must be stored for later retrieval.

# planning:
# class Contact will define a person and their contact information
# different methods to view all, search for, add, delete, modify contacts
# program should ask you what you want to do, at beginning, when viewing all, and when viewing a specific contact

# work flow notes:

# ver 1: address_book was a list of contacts. name of object was person's name,
#   but was separate from their actual name, which would make it difficult to create new contacts --
#   would have to define both name of person object and name of person
# ver 2: use dictionary instead. that way name is key and can be more easily accessed and manipulated
# ver 3: got dictionary of contacts to work, by storing multiple details as a list, then the list is the single value
#   for the name key. implemented pickle and storage of contacts
# ver 4: added "group" classification to contacts so they could be sorted by type


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
    """Allows the user to view the entire address book"""
    # returns a list of names
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    print("\nContacts in Address Book:")
    for names, details in stored_contacts.items():
        print(names)


def view():
    """Allows the user to view all contact details of a contact"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    person = input("Who's contact details would you like to view? ")
    for names, details in stored_contacts.items():
        if person in names:
            print("\nName: {}, Number: {}, Email: {}\n".format(names, details[0], details[1]))
            break
        else:
            print("No contact {} exists.".format(person))


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
    elif type == "group":
        group = input("Which group would you like to view? [friends], [family], or [colleagues]: ")
        print("\nThe contacts in group '{}' are: ".format(group))
        for names, details in stored_contacts.items():
            if group == details[2]:
                print(names)
        print("\n")


def add():
    """Allows the user to add someone to the address book"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)


def delete(contact):
    """Allows the user to delete a contact"""
    f = open(address_book_file, "rb")
    stored_contacts = pickle.load(f)
    contact = input("Who would you like to delete? ")
    del address_book[contact]

while True:
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
        delete()
    elif action == "add":
        add()
    else:
        print("Unknown action")
