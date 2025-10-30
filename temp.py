def convert_temperature(value, unit):
    unit = unit.lower()

    if unit == 'celsius' or unit == 'c':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin

    elif unit == 'fahrenheit' or unit == 'f':
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin

    elif unit == 'kelvin' or unit == 'k':
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit

    else:
        raise ValueError("Invalid unit! Please enter Celsius, Fahrenheit, or Kelvin.")


def main():
    print("=== Temperature Converter ===")
    try:
        temp_value = float(input("Enter the temperature value: "))
        temp_unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ").strip()

        if temp_unit.lower() in ['c', 'celsius']:
            fahrenheit, kelvin = convert_temperature(temp_value, temp_unit)
            print(f"\n{temp_value:.2f} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")

        elif temp_unit.lower() in ['f', 'fahrenheit']:
            celsius, kelvin = convert_temperature(temp_value, temp_unit)
            print(f"\n{temp_value:.2f} °F = {celsius:.2f} °C = {kelvin:.2f} K")

        elif temp_unit.lower() in ['k', 'kelvin']:
            celsius, fahrenheit = convert_temperature(temp_value, temp_unit)
            print(f"\n{temp_value:.2f} K = {celsius:.2f} °C = {fahrenheit:.2f} °F")

        else:
            print("Invalid unit! Please enter Celsius, Fahrenheit, or Kelvin.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
