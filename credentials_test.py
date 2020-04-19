import unittest
import pyperclip
from credentials import Credential

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        """Set up method to run before each test cases.
        """
        self.new_credential = Credential('Maureen', 'Nimoh' , 'nimoh@yahoo.com', 'nimx12')
        
    def test_init(self):
        self.assertEqual(self.new_credential.credentialName, 'Maureen')
        self.assertEqual(self.new_credential.userName, 'Nimoh')
        self.assertEqual(self.new_credential.email, 'nimoh@yahoo.com')
        self.assertEqual(self.new_credential.password, 'nimx12')
        
    def test_save_credential(self):
        self.new_credential.save_credential()  
        self.assertEqual(len(Credential.credential_list), 1)


    