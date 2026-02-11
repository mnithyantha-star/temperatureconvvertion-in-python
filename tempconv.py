print("Temperatures Conversion Program")
print("choose the unit you are entering:")
print("1.Celsius")
print("2.Fahrenheit")
print("3.Kelvin")

choice = int(input("Enter choice (1/2/3): "))
temp = float(input("Enter temperature value: "))

if choice == 1:
  fahrenheit = (temp * 9/5) + 32
  kelvin = temp + 273.15
  print("Fahrenheit:", fahrenheit)
  print("Kelvin:",kelvin)

elif choice == 2:
  celsius = (temp - 32) * 5/9
  kelvin = celsius + 273.15
  print("Celsius:",celsius)
  print("Kelvin:",kelvin)

elif choice == 3:
  celsius = temp - 273.15
  fahrenheit = (celsius * 9/5) + 32
  print("Celsius:", celsius)
  print("Fahrenheit:",fahrenheit)

else:
  print("Invalid choice")
