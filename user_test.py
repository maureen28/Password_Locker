import unittest  # Import unittest module
import pyperclip
from user import User


class TestUser(unittest.TestCase):
    """ Defines test cases for the User class behavior """

    def setUp(self):
        self.new_user = User('Mutahi', 'Kimani', 'mkimz', 'mutahi@gmail.com', 'Mtuh123')

    def test_init(self):
        self.assertEqual(self.new_user.firstName, 'Mutahi')
        self.assertEqual(self.new_user.lastName, 'Kimani')
        self.assertEqual(self.new_user.userName, 'mkimz')
        self.assertEqual(self.new_user.email, 'mutahi@gmail.com')
        self.assertEqual(self.new_user.password, 'Mtuh123')

    def test_save_user(self):
        self.new_user.save_user()  # save the new user
        self.assertEqual(len(User.user_details), 1)

    def tearDown(self):
        User.user_details = []

    def save_multiple_users(self):
        self.new_user.save_user()
        test_user = User('Facebook', 'Moh', 'nimoh', '@foodie', 'foodzone')
        test_user.save_user()
        self.assertEqual(len(User.user_details), 2)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User('Facebook', 'Moh', 'nimoh', '@foodie', 'foodzone')
        test_user.save_user()
        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_details), 1)

    def find_user_by_username(self):
        self.new_user.save_user()
        test_user = User('Facebook', 'Moh', 'nimoh', '@foodie', 'foodzone')
        test_user.save_user()

        found_user = User.find_by_username('nimoh')
        self.assertEqual(found_user.userName, test_user.userName)

    def test_user_exists(self):
        """Checking if we can return a Boolean if we can't find the user
        """
        self.new_user.save_user()
        test_user = User('Facebook', 'Moh', 'nimoh', '@foodie', 'foodzone')
        test_user.save_user()
        
        user_exists = User.user_exist('nimoh')
        
        self.assertTrue(user_exists)

if __name__ == "__main__":
    unittest.main()
