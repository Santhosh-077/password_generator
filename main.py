import secrets
import string
def get_password_length():
    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
            else:
                return length

        except ValueError:
            print("Please enter a valid number.")

def get_character_choices():
    print("\nChoose character types:")
    print("1. Uppercase Letters (A-Z)")
    print("2. Lowercase Letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!, @, #, etc.)")
    while True:
        choices = input(
            "\nEnter your choices (Example: 1234 or 23): "
        ).strip()

        choices = "".join(dict.fromkeys(choices))

        valid_choices = {"1", "2", "3", "4"}

        if not choices or not set(choices).issubset(valid_choices):
            print("Please enter only 1, 2, 3, or 4.")
            continue

        if len(choices) < 2:
            print("Please select at least 2 character types.")
            continue

        return choices

def generate_password(length, choices):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    characters = ""
    password = []

    if "1" in choices:
        characters += uppercase
        password.append(secrets.choice(uppercase))

    if "2" in choices:
        characters += lowercase
        password.append(secrets.choice(lowercase))

    if "3" in choices:
        characters += numbers
        password.append(secrets.choice(numbers))

    if "4" in choices:
        characters += symbols
        password.append(secrets.choice(symbols))

    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


print("=" * 45)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:

    length = get_password_length()
    choices = get_character_choices()

    password = generate_password(length, choices)

    print("\n" + "=" * 45)
    print("GENERATED PASSWORD:")
    print(password)
    print("=" * 45)

    while True:

        again = input(
            "\nDo you want to generate another password? (Y/N): "
        ).strip().lower()

        if again == "y":
            break

        elif again == "n":
            print("\nThank you for using the Password Generator.")
            print("Stay secure!")
            exit()

        else:
            print("Please enter Y or N.")