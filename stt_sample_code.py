'''
    Sample Code as part of STT Lab 1
'''


def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")


def main():
    """Run greetings for multiple people."""
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for name in names:
        greet(name)

    numbers = list(range(1, 11))
    total = sum(numbers)
    print(f"The sum of numbers from 1 to 10 is {total}")

    squares = {n: n ** 2 for n in numbers}
    print("Squares of numbers:", squares)

    print("Script finished successfully.")


if __name__ == "__main__":
    main()
