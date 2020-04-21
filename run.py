#!/usr/bin/env python3.6

from user import User
from credentials import Credential

# User
def create_user(firstName, lastName, userName, email, password):
    """ Function create a new user
    """
    new_user = User(firstName, lastName, userName, email, password)
    return new_user

def save_user(user):
    """Function to save user"""
    user.save_user()

def del_user(user):
    """Function to delete a user"""
    user.delete_user()

def find_user(userName):
    return User.find_by_username(userName)

def check_user_exist(userName):
    return User.user_exist(userName)

def display_users():
    return User.display_users()

# credentials
def create_credentials(credentialName, userName, email, password):
    new_credential = Credential(credentialName, userName, email, password)
    return new_credential

def save_credential(credential):
    credential.save_credential()

def del_credential(credential):
    credential.delete_credential()

def find_credential(credentialName):
    return Credential.find_by_credentialName(credentialName)

def check_credential_exist(credentialName):
    return Credential.credential_exist(credentialName)

def display_credential():
    return Credential.display_credential()

# def copy_credential(credentialName):
# 	'''
# 	Function to copy a credentials details to the clipboard
# 	'''
# 	return Credential.copy_credential(credentialName)

# Main
def main():
    print("Hello! Welcome to my Password Locker. What is your name?")
    user_name = input()
    
    print(f"Hello {user_name}. Let's get you started with Password Locker")
    print('\n')

    while True:
        print("Use these short codes : su- Sign up,\n  du -Display details,\n lo - login details \n ex -exit the Password Locker ")
        short_code = input().lower()
        
        if short_code == 'su':
            print("Create a new account")
            print("-"*100)

            print ("First name ....")
            firstName = input()

            print("Last name ...")
            lastName = input()
                            
            print("User name ...")
            userName = input()

            print("Email address ...")
            email = input()
                
            print("Password ...")
            password = input()

            save_user(create_user(firstName, lastName, userName, email, password)) # create and save new contact.
            print ('\n')
            print(f"New user {firstName} {lastName} created")
            print ('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is your account and your details ")
                print('\n')

                for user in display_users():
                    print(f"{user.firstName} {user.lastName} ..{user.userName}")
                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any user account saved yet")
                    print('\n')

        elif short_code == 'lo':

            print("Enter the password to login")
            u_name = input()
            if check_user_exist(u_name):
                search_user = find_user(u_name)
                print()
                print(f"{search_user.userName} is logged in")
                print()                        
 
                while True:
                    print("Use these short codes : cc- Create new credential,\n D -Display credentials, del - delete credential \n ex -Log out ")
                    short_code = input().lower()
         
                    if short_code == 'cc':
                        print("Create your credentials")
                        print("-"*100)       
                        print("Credential name ...")
                        credential_name = input()               
                        print("User name ...")
                        user_name = input()
                        print("Email address ...")
                        email = input()
                        
                        print("Please choose an option for entering a passsword: e - enter password \n gp- generate a password.")
                        password = input('Enter an option: ')
                        # if pass_choice == 'e':
						# 		print(" ")
						# 		pass_choice = input('Enter your password: ')
						# 		break
						# else:
						# 		pass_choice = generate_password()
						# 		break
							
                        save_credential(create_credentials(credential_name, user_name, email, password)) 
                        print ('\n')
                        print(f"Your credentials  {credential_name} have been created")
                        print ('\n')

                    elif short_code == 'D':
                        if display_credential():
                            print("Here is your credential")
                            print('\n')
                            
                            for credential in display_credential():
                                print(f"Credential name:{credential.credential_name}  User name: {credential.user_name} Password:{credential.password}")
                                print('\n')
                        else:
                            print('\n')
                            print("You don't seem to have created any credentials yet")
                            print('\n')
                            
                    # elif short_code == "del":
                    #         if del_credential():
                    #             print("Are you sure you want to delete your account? ")
                    #             print('\n')      
                    #             for credential in del_credential(credential):
                    #                     print(f"Credential name:{credential.credential_name} has been successfully deleted")
                    #                     print('\n')
                                        
                    #         else:
                    #             print('\n')
                    #             print("You might have put the wrong username or password. Please try again!")
                    #             print('\n')
                                
                    # elif short_code == 'copy':
                    #             print('')
                    #             chosen_site = input('Enter the credential name for the credential password to copy: ')
                    #             copy_credential(chosen_site)
                    #             print('')
					#         else:
					# 	        print('Oops! Wrong option entered. Try again.')

                    elif short_code == "ex":
                        print('\n')
                        print(f"You have logged out your {credential_name} account")
                        print('\n')
                        break
                           
        elif short_code == "ex":
                    print(f"Thanks {user_name} for your time.I hope you enjoyed my service.Bye...")
                    break
        else:
                    print("I really didn't get that. Please use the short codes")

                  
if __name__ == "__main__":
    main()