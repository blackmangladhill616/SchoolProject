def get_random_code():
    import random
    numbers = '123456789'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()'
    code = ''
    for i in range(random.randint(1, 8)):
        code += random.choice(numbers)
    for i in range(random.randint(1, 8)):
        code += random.choice(letters)
    for i in range(random.randint(1, 8)):
        code += random.choice(symbols)
    return code
