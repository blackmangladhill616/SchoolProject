import random
def get_random_code(length=8):
    chars = "abcdefghijklmnopqrstuvwxyz"
    code = ''
    for _ in range(length):
        code += random.choice(chars)
    return code