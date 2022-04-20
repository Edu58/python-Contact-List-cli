# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
import pyperclip
from blueprint import Contact


class TestContact(unittest.TestCase):
    def setUp(self):
        self.new_contact = Contact('Edwin', 'Karimi', '0718471455', 'edu@gmail.com')

    def tearDown(self):
        Contact.contact_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_contact.first_name, "Edwin")
        self.assertEqual(self.new_contact.last_name, "Karimi")
        self.assertEqual(self.new_contact.phone_number, "0718471455")
        self.assertEqual(self.new_contact.email, "edu@gmail.com")

    def test_save_contact(self):
        """
        the contact list test_save_contact test case to test if the contact object is saved into
        """
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_save_multiple_contacts(self):
        self.new_contact.save_contact()
        test_contact = Contact('Test', 'testing', '0700000000', 'test@gmail.com')
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_test(self):
        self.new_contact.save_contact()
        test_contact = Contact('Test', 'testing', '070000000', 'testing@gmail.com')
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        self.new_contact.save_contact()
        test_contact = Contact('test', 'tester', '07000000', 'eddy@gmail.com')
        test_contact.save_contact()

        found_contact = Contact.find_by_number('07000000')

        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact = Contact('Test', 'testing', '07000000', 'tester@gmail.com')
        test_contact.save_contact()

        contact_exists = Contact.contact_exists('07000000')
        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    def test_copy_email(self):
        self.new_contact.save_contact()
        Contact.copy_email("0718471455")

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
