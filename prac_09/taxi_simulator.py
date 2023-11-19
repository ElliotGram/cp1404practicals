"""
CP1404/CP5632 Practical
taxi simulator
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display information about available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Allow the user to choose a taxi."""
    display_taxis(taxis)
    choice = input("Choose taxi: ")
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(taxis):
            return taxis[choice]
    print("Invalid taxi choice")
    return None

def drive_taxi(taxi):
    """Simulate driving a taxi."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        distance = float(input("Drive how far? "))
        fare = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare

def main():
    print("Let's drive!")
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()

        if user_choice == 'q':
            break
        elif user_choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif user_choice == 'd':
            fare = drive_taxi(current_taxi)
            if fare is not None:
                total_bill += fare
        else:
            print("Invalid option")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()