FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32)* FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature():
    try:
        return float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return None

choose_value = get_temperature()


choose_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if choose_unit.upper() == "C":
    converted_value = convert_to_fahrenheit(choose_value)
    print(f"{choose_value}°C is {converted_value}°F")
elif choose_unit.upper() == "F":
    converted_value = convert_to_celsius(choose_value)
    print(f"{choose_value}°F is {converted_value}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


