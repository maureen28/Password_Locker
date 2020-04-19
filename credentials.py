class Credentials:
     """Class that generates new instances of the user-credentials
    """
    credential_list =[]
    
    def __init__(self, firstName, lastName, userName, email, password):
        """__init__ method helps us instantiate
        """
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.email = email
        self.password = password