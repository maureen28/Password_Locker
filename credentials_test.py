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

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential('Miriam', 'Leo', 'lee@yahoo.com', '12pril')
        test_credential.save_credential()
        self.new_credential.delete_credential()  # Deleting a credential object
        self.assertEqual(len(Credential.credential_list), 1)

    def find_credential_by_credentialName(self):
        self.new_credential.save_credential()
        test_credential = Credential('Miriam', 'Leo', 'lee@yahoo.com', '12pril')
        test_credential.save_credential()

        found_credential = Credential.find_by_credentialName('nimoh')
        self.assertEqual(found_credential.credentialName, test_credential.credentialName)

    def test_credential_exists(self):
        """Checking if we can return a Boolean if we can't find the credential
        """
        self.new_credential.save_credential()
        test_credential = Credential('Miriam', 'Leo', 'lee@yahoo.com', '12pril')
        test_credential.save_credential()
        
        credential_exists = Credential.credential_exist('Miriam')
        
        self.assertTrue(credential_exists)
        
    def test_display_credential(self):
        """ Return a list of all credentials saved"""
        self.assertEqual(Credential.display_credential(), Credential.credential_list)
        
    # def test_copy_credential(self):
	#     self.new_credential.save_credential()
	# 	fb = Credential('Mir', 'Le', 'le@yahoo.com', '12pril')
	# 	fb.save_credentials()
  
	# 	find_credential = None
	# 	for credential in Credential.credential_list:
	# 		find_credential = Credential.find_by_credentialName(credentialName)
	# 			return pyperclip.copy(find_credential.password)

	# 	Credential.copy_credential(self.new_credential.credentialName)
	# 	self.assertEqual('12pril',pyperclip.paste())
	# 	print(pyperclip.paste())

if __name__ == "__main__":
    unittest.main()
