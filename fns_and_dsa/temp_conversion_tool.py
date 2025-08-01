FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
while True:
    try:
        temp = float(input("Enter the temperature to convert:"))
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

def convert_to_celsius(fahrenheit):
    temp_in_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_in_celsius
def convert_to_fahrenheit(celsius):
    temp_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp_in_fahrenheit


unit = (input("Is this temperature in Celsius or Fahrenheit? (C/F):")).upper()
if unit == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
elif unit == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")