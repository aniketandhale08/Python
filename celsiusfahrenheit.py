def celsius_to_fahrenheit(celsius):
    return (celsius *9/5)+32

celsius = int(input("Enter the celsius to convert it to fahrenheit: "))
fahrenheit =celsius_to_fahrenheit(celsius)

print(f"The conversion of {celsius}°C to fahrenheit is {fahrenheit}°F")