#!/usr/bin/env python3.6

from user import User
from credentials import Credential

def create_user(user_name,email,password):
    """ Function create a new user
    """
    new_user = User(user_name,email,password)
    return new_user

def save_user(user):
    """Function to save contact"""
    user.save_user()
    
def del_user(user):
    """Function to delete a user"""
    user.delete_user()