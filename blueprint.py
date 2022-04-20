import pyperclip


class Contact:
    """
    class that generates new instances of contacts
    """

    # This is a class variable
    contact_list = []

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls, number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exists(cls, number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True

    @classmethod
    def display_contacts(cls):
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        contact_found = cls.find_by_number(number)
        pyperclip.copy(contact_found.email)

    def __init__(self, first_name, last_name, phone_number, email):
        """
        __init__ method helps us define properties for our objects
        Args:
            first_name: New contact first name.
            last_name : New contact last name.
            phone_number: New contact phone number.
            email : New contact email address.
        """
        # These are instance variables`
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
