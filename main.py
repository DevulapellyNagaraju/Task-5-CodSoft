from contact_book import ContactBook

def main():
    contact_book = ContactBook()

    while True:
        # Print formatted title "Contact Book"
        print('\033[2m' + '\033[1m' + ' ࿇ =  = Contact Book =  = ࿇' + '\033[0m')
        
        # Print menu options
        print('\033[95m' + '\nContact Book Menu:' + '\033[0m')
        print('\033[93m' + '1. Add Contact' + '\033[0m')
        print('\033[93m' + '2. View Contacts' + '\033[0m')
        print('\033[93m' + '3. Search Contact' + '\033[0m')
        print('\033[93m' + '4. Update Contact' + '\033[0m')
        print('\033[93m' + '5. Delete Contact' + '\033[0m')
        print('\033[93m' + '6. Exit' + '\033[0m')

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank and enter to keep current): ")
            contact_book.update_contact(name, new_phone if new_phone else None, new_email if new_email else None)

        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book.")
            break

        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    main()
