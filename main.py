# Interactive Calculator & Unit Converter

def calculator():
    print("\n--- Calculator ---")
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result =", num1 + num2)
    elif op == "-":
        print("Result =", num1 - num2)
    elif op == "*":
        print("Result =", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operator!")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose an option (1-2): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")

    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")

    else:
        print("Invalid choice!")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("1. INR to USD")
    print("2. USD to INR")

    choice = input("Choose an option (1-2): ")

    # Example exchange rate (change if required)
    rate = 87.0

    if choice == "1":
        inr = float(input("Enter amount in INR: "))
        print(f"{inr:.2f} INR = {inr / rate:.2f} USD")

    elif choice == "2":
        usd = float(input("Enter amount in USD: "))
        print(f"{usd:.2f} USD = {usd * rate:.2f} INR")

    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            unit_converter()

        elif choice == "3":
            currency_converter()

        elif choice == "4":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid input! Please enter a number between 1 and 4.")


# Run the program
main()