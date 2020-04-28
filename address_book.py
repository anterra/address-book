#prompt: create your own command-line address-book program using which you can
#browse, add, modify, delete or search for your contacts such as friends, family and colleagues
#and their information such as email address and/or phone number.
#details must be stored for later retrieval.

#planning:
#class Contact will define a person and their contact information
#different methods to view all, search for, add, delete, modify contacts
#program should ask you what you want to do, at beginning, when viewing all, and when viewing a specific contact

#work flow notes:
#ver 1: had a list of contacts. name of object was person's name, but was separate from their actual name, which would
    #make it difficult to create new contacts -- would have to define both name of person object and name of person
#ver 2: going to use dictionary. that way name is key and can be more easily accessed and manipulated


class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def view(self):
        """Allows the user to view all contact details of a contact"""
        person = input("Who's contact details would you like to view? ")
        for contacts in address_book:
            if person in contacts.name:
                print("Name: {}, Number: {}, Email: {}".format(contacts.name, contacts.number, contacts.email))
                break
            else:
                print("No contact {} exists.".format(person))

def browse():
    """Allows the user to view the entire address book"""
    # returns a list of names
    print("Contacts in Address Book:")
    for contacts in address_book:
        print(contacts.name)

def search():
    """Allows the user to search the address book for a certain person or group of people"""
    person = input("Who are you searching for? ")
    for contacts in address_book:
        if contact == contacts.name:
            proceed = input("Found contact {}. Would you like to view their contact information? ".format(contact))
            if proceed == "yes":
                person.view()
            else:
                break


def add(contact):
    """Allows the user to add someone to the address book"""

    #print("{} has been added.".format(newcontact.name))

def delete(contact):
    """Allows the user to delete some"""




#contacts
address_book = {
    "Liz": "402.7297", "liz@gmail.com", "friend",
    "Devon": "461.9025", "devon@gmail.com", "friend",
    "Dad": "301.0250", "dad@gmail.com", "family",
    "Hope": "620.0863", "hope@gmail.com", "family",
    "James": "208.3246", "james@gmail.com", "colleague"
    "Laura": "516.0275", "laura@gmail.com", "colleague"
}


while True:
    contact = Contact("", "", "", "")
    action = input("""What would you like to do?: 
            [browse] address book
            [view] a contact
            [search] for someone
            [add] someone new
            [delete] someone
            [quit] --> """)
    if action == "quit":
        break
    if action == "browse":
        browse()
    if action == "view":
        contact.view()
    if action == "search":
        search()
    #if action == "add":


