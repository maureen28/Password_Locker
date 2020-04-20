import pyperclip
class User:
    """Class that generates new instances of the user
    """
    user_details = []  # Empty user list

    def __init__(self, firstName, lastName, userName, email, password):
        """__init__ method helps us instantiate
        """
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.email = email
        self.password = password

    def save_user(self):
        """ Save our user object to our user details
        """
        User.user_details.append(self)
  
    def delete_user(self):
        User.user_details.remove(self)
        
    @classmethod
    def find_by_username(cls, userName):
        for user in cls.user_details:
            if user.userName == userName:
              return user
          
    @classmethod
    def user_exist(cls, userName):
        """Check and view if the user exists in the user-details
        """
        for user in cls.user_details:
            if user.userName == userName:
               return True
        return False
    
    @classmethod
    def display_users(cls):
        return cls.user_details
        
    @classmethod
    def copy_password(cls, password):
        user_found = User.find_by_password(password)
        pyperclip.copy(user_found.password)