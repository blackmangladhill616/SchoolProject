import random

def get_random_number(n):
    return random.randint(1, n)

def main():
    number = get_random_number(20)
    print(f"Random number between 1 and 20: {number}")

if __name__ == "__main__":
    main()
