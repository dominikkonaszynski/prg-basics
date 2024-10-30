###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celcius = int(input("Enter the temperature in degrees Celcius: "))
kelvin = celcius + 273
fahrenheit = (celcius * 1.8) + 32
print (f"{celcius} degrees celcius is {kelvin} kelvins and {fahrenheit} fahrenheits")