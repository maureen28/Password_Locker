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

# Main
def main():
      print("Hello! Welcome to my Password Locker. What is your name?")
      user_name = input()

      print(f"Hello {user_name}. what would you like to do?")
      print('\n')

      while True:
        print("Use these short codes :\n su- Sign up,\n si - Sign in,\n p -Display details,\n ex -exit the Password Locker ")
        short_code = input().lower()
        if short_code == 'su':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')
