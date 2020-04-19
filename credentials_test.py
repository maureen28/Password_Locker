import unittest
import pyperclip
from credentials import Credential


class TestCredentials(unittest.TestCase):

    def setUp(self):
        """Set up method to run before each test cases.
        """
        self.new_credential = Credential('Maureen', 'Nimoh', 'nimoh@yahoo.com', 'nimx12')

    def test_init(self):
        self.assertEqual(self.new_credential.credentialName, 'Maureen')
        self.assertEqual(self.new_credential.userName, 'Nimoh')
        self.assertEqual(self.new_credential.email, 'nimoh@yahoo.com')
        self.assertEqual(self.new_credential.password, 'nimx12')

    def test_save_credential(self):

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential('Miriam', 'Leo', 'lee@yahoo.com', '12pril')
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def tearDown(self):
        Credential.credential_list = []

    def test_delete_user(self):
        self.new_credential.save_credential()
        test_credential = Credential('Miriam', 'Leo', 'lee@yahoo.com', '12pril')
        test_credential.save_credential()
        self.new_credential.delete_credential()  # Deleting a credential object
        self.assertEqual(len(Credential.credential_list), 1)
