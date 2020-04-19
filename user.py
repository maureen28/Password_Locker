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