import random

def get_random_code(length):
    code = ""
    for i in range(length):
        code += chr(ord('A') + random.randint(0, 25))
    return code

print(get_random_code(10))
