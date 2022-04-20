from blueprint import Contact


def create_contact(f_name, l_name, p_number, email):
    """
    Function to create a new contact
    """
    new_contact = Contact(f_name, l_name, p_number, email)
    return new_contact


def save_contacts(contact):
    contact.save_contact()


def del_contact(contact):
    contact.delete_contact()


def find_contact(number):
    """
    Function that finds a contact by number and returns the contact
    """
    return Contact.find_by_number(number)


def check_existing_contacts(p_number):
    return Contact.find_by_number(p_number)


def display_contacts():
    return Contact.display_contacts()


def main():
    print("Hello and welcome to your contact list. what is your name?")
    username = input()

    print("Hello {}. What would you like to do?".format(username))
    print('\n')

    while True:
        print(
            "Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, "
            "del - delete a contact, ex -exit the contact list")

        short_code = input().lower()

        if short_code == 'cc':
            print("New contact")
            print("-" * 10)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            save_contacts(create_contact(f_name, l_name, p_number, e_address))  # create and save new contact.
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print('\n')

        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_contact.phone_number}")
                print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")

        elif short_code == 'del':
            print('Enter phone number of the contact to delete:')

            number_to_delete = input()

            del_contact(find_contact(number_to_delete))
            print('Contact deleted successfully')

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
