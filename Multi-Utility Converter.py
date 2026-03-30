def convert_weight():
    print("\n--- Weight Converter ---")
    print("1. Kilograms (kg) to Pounds (lbs)")
    print("2. Pounds (lbs) to Kilograms (kg)")

    try:
        choice = input("Enter choice (1 or 2): ")
        val = float(input("Enter weight value: "))

        if choice == '1':
            ans = val * 2.20462
            print(f"Result: {val} kg = {round(ans, 2)} lbs")
        elif choice == '2':
            ans = val / 2.20462
            print(f"Result: {val} lbs = {round(ans, 2)} kg")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Error: Please enter a valid number.")

def convert_length():
    print("\n--- Length Converter ---")
    print("1. Kilometers (km) to Miles")
    print("2. Miles to Kilometers (km)")

    try:
        choice = input("Enter choice (1 or 2): ")
        val = float(input("Enter length value: "))

        if choice == '1':
            ans = val * 0.621371
            print(f"Result: {val} km = {round(ans, 2)} miles")
        elif choice == '2':
            ans = val / 0.621371
            print(f"Result: {val} miles = {round(ans, 2)} km")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Error: Please enter a valid number.")

def convert_volume():
    print("\n--- Volume Converter ---")
    print("1. Liters to Gallons (US)")
    print("2. Gallons (US) to Liters")

    try:
        choice = input("Enter choice (1 or 2): ")
        val = float(input("Enter volume value: "))

        if choice == '1':
            ans = val * 0.264172
            print(f"Result: {val} Liters = {round(ans, 2)} Gallons")
        elif choice == '2':
            ans = val * 3.78541
            print(f"Result: {val} Gallons = {round(ans, 2)} Liters")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Error: Please enter a valid number.")

def convert_temp():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = input("Enter choice (1 or 2): ")

        if choice == '1':
            val = float(input("Enter Temp in Celsius: "))
            ans = (val * 1.8) + 32
            print(f"Result: {val}°C = {round(ans, 2)}°F")
        elif choice == '2':
            val = float(input("Enter Temp in Fahrenheit: "))
            ans = (val - 32) / 1.8
            print(f"Result: {val}°F = {round(ans, 2)}°C")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    while True:
        print("\n=============================")
        print("   MULTI-UTILITY CONVERTER   ")
        print("=============================")
        print("1. Weight (Kg / Lbs)")
        print("2. Length (Km / Miles)")
        print("3. Volume (Liters / Gallons)")
        print("4. Temperature (°C / °F)")
        print("5. Exit")

        selection = input("Choose a category (1-5): ")

        if selection == '1':
            convert_weight()
        elif selection == '2':
            convert_length()
        elif selection == '3':
            convert_volume()
        elif selection == '4':
            convert_temp()
        elif selection == '5':
            print("Exiting program. Have a nice day!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
