
# Exercise 1: Temperature Converter

def Fahrenheit(temp):   # function to convert fahrenheit into celsius
    return  5/9 * (temp - 32)
    

def Celsius(temp):      # function to convert celsius into fahrenheit
    return 9/5 *temp + 32


temp = float(input("Enter the temperature: "))
degree = input("Is the temperature in C or F?: ").upper()
if degree == 'C':                         # check if the given temperature in is celsius or fahrenheit
    converted = Celsius(temp)
    print(f"The Celsius value is {converted:.f}")  # if celcius, print the converted to fahrenheit value
elif degree == 'F':
    converted = Fahrenheit(temp)
    print(f"The Fahrenheit value is {converted:.2f}") # if fahrenheit, print the converted to celsius value
else:
    print("Wrong value. Put in 'C' or 'F'")   # if wrong input, send error message