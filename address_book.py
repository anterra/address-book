#prompt: create your own command-line address-book program using which you can
#browse, add, modify, delete or search for your contacts such as friends, family and colleagues
#and their information such as email address and/or phone number.
#details must be stored for later retrieval.

#planning:
#different classes to view all, search for, add, delete, modify contacts
#program should ask you what you want to do, at beginning, when viewing all, and when viewing a specific contact

class Contact:

    def __init__(self, name, number, email, group):
        self.name = name
        self.number = number
        self.email = email
        self.group = group

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
Liz = Contact("Liz", "502.7298", "liz@gmail.com", "friend")
Devon = Contact("Devon", "561.9026", "devon@gmail.com", "friend")
Dad = Contact("Dad", "401.0251", "dad@gmail.com", "family")
Hope = Contact("Hope", "720.0864", "hope@gmail.com", "family")
James = Contact("James", "308.3247", "james@gmail.com", "colleague")
Laura = Contact("Laura", "616.0276", "laura@gmail.com", "colleague")

address_book = [Liz, Devon, Dad, Hope, James, Laura]

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


