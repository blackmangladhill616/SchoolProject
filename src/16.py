import random
def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Parameters:
        length (int): The length of the generated string.
        
    Returns:
        str: A random string of the given length.
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
