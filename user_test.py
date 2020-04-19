import unittest  # Import unittest module
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    """ Defines test cases for the User class behavior """
    def setUp(self):
       self.new_user = User('Mutahi','Kimani','mkimz','mutahi@gmail.com','Mtuh123')