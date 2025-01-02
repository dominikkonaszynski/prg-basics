class Contact():
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone
    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Telephone: {self.telephone}"

class Contact_List():
    def __init__(self):
        self.contacts = []

    def add_contact(self,contact):
        self.contacts.append(contact)

    def display_contact(self):
        for contact in self.contacts:
            print(contact)

def main():
    contact_list = Contact_List()
    contact1 = Contact("John Brown", "brown@onet.pl", "555234000")
    contact_list.add_contact(contact1)
    contact_list.display_contact()

if __name__ == "__main__":
    main()