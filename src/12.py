import random
def get_random_code():
    """
    Generates a random 5-digit code
    """
    code = ''
    while len(code) < 5:
        code += str(random.randint(0, 9))
    return code