import random
import string


def generate_password(upper=0, lower=0, digits=0, symbols=0):
    if upper < 0 or lower < 0 or digits < 0 or symbols < 0:
        raise ValueError("All counts must be non-negative")

    upper_chars = [random.choice(string.ascii_uppercase) for _ in range(upper)]
    lower_chars = [random.choice(string.ascii_lowercase) for _ in range(lower)]
    digit_chars = [random.choice(string.digits) for _ in range(digits)]
    symbol_chars = [random.choice(string.punctuation) for _ in range(symbols)]

    password_chars = upper_chars + lower_chars + digit_chars + symbol_chars
    random.shuffle(password_chars)

    return ''.join(password_chars)


if __name__ == "__main__":
    print(generate_password(upper=7, lower=4, digits=2, symbols=10))
