
import random

def get_random_code():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    code = ''
    for i in range(5):
        code += random.choice(alphabet)
    return code