'''
Chapter 2
Zynab Ali
'''

#Convert Celsius to Fahrenheit
temp_celsius = float(input('\nEnter temperature in Celsius: '))

def celsuis_to_fahrenheit(celsius):
    """Equation for Fahrenheit conversion"""
    return (9/5)*celsius + 32

temp_fahrenheit = celsuis_to_fahrenheit(temp_celsius)

print(f"Temperature in Fahrenheit: {temp_fahrenheit:.1f}°F\n")
