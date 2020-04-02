# We have provided a list of temperatures in celsius. Using a list comprehension, create a new list called fahrenheit that converts each element in the celsius list to fahrenheit.

# *Note: * To convert, use the formula:
# temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp * 9/5 + 32 for temp in celsius ]
print(fahrenheit)
