import random

def generate_random_number(start, end):
    return random.randint(start, end)

def main():
    print("Welcome to the Random Number Generator!")
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))

    random_number = generate_random_number(start, end)
    print(f"Random number between {start} and {end}: {random_number}")

if __name__ == "__main__":
    main()
