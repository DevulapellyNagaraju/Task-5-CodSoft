class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        print("\033[92m" + f"Contact of {name} added successfully." + "\033[0m")

    def view_contacts(self):
        if not self.contacts:
            print("\033[91mNo contact found.\033[0m")
        else:
            for i, contact in enumerate(self.contacts):
                print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower()]
        if not found_contacts:
            print("\033[91mNo contact found.\033[0m")
        else:
            print("\033[92mSearch of contact found!\033[0m")  # Green color for found message
            for i, contact in enumerate(found_contacts):
                print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                print("\033[92mYour contact has been updated!\033[0m")
                return
                
        print("\033[91mContact not found.\033[0m")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                print('\033[92m' + f"Contact of {name} deleted successfully." + '\033[0m' )
                return
        print("\033[91mContact not found.\033[0m")
