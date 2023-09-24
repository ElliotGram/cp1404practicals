MINIMUM_LENGTH = 4

password = input("Enter Password: ")

while len(password) < minimum_length:
    print("Password too short please try again")
    password = input("Enter Password: ")

print("*" * len(password))