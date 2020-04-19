class Credential:
    """Class that generates new instances of the credentials
    """
    credential_list = []  # Empty credential list

    def __init__(self, credentialName, userName, email, password):
      
        self.credentialName = credentialName
        self.userName = userName
        self.email = email
        self.password = password
        
     def save_user(self):
        """ Save our credential object to our user details
        """
        User.user_details.append(self)
   