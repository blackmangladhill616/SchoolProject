import random

def get_random_number(n):
    """Returns a random number between 1 and n"""
    return random.randint(1, n)

def get_random_string(length):
    """Returns a random string of length characters"""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += random.choice(letters)
    return result

def get_random_number_list(n, length):
    """Returns a list of n random numbers between 1 and length"""
    return [get_random_number(length) for i in range(n)]

def get_random_string_list(n, length):
    """Returns a list of n random strings of length characters"""
    return [get_random_string(length) for i in range(n)]