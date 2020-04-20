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
