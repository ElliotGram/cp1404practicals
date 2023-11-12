MENU = """
Temperature Conversion Menu:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
"""

def main():
    print(MENU)
    choice = input("Choice: ")

    if choice == '1':
        celsius_value = float(input("Enter temperature in Celsius: "))
        fahrenheit_result = celsius_to_fahrenheit(celsius_value)
        print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_result} degrees Fahrenheit.")
    elif choice == '2':
        fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
        celsius_result = fahrenheit_to_celsius(fahrenheit_value)
        print(f"{fahrenheit_value} degrees Fahrenheit is equal to {celsius_result} degrees Celsius.")
    else:
        print("Invalid choice. Please enter 1 or 2.")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


main()
