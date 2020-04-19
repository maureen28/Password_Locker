class Credential:
    """Class that generates new instances of the credentials
    """
    credential_list = []  # Empty credential list

    def __init__(self, credentialName, userName, email, password):

        self.credentialName = credentialName
        self.userName = userName
        self.email = email
        self.password = password

    def save_credential(self):
        """ Save our credential object to our user details
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_credentialName(cls, credentialName):
        for credential in cls.credential_list:
            if credential.credentialName == credentialName:
                return credential

    @classmethod
    def credential_exist(cls, credentialName):
        """Check and view if the user exists in the user-details
        """
        for credential in cls.credential_list:
            if credential.credentialName == credentialName:
                return True
        return False

    @classmethod
    def display_credential(cls):
        return cls.credential_list
