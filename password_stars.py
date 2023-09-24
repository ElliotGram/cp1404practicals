MINIMUM_LENGTH = 4


def main():
    password = get_password()
    print_password_asterisks(password)


def get_password():
    password = input("Enter Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password too short. Please try again.")
        password = input("Enter Password: ")
    return password


def print_password_asterisks(password):
    print("*" * len(password))


main()
