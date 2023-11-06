import calcModule

number_1 = input("Enter first number: ")
number_2 = input("Enter second number: ")
operat = input("Would you like to add, subtract, multiply or divide: ")

number_1 = float(number_1)
number_2 = float(number_2)
operat = operat.lower()

if operat == "add":
   result = calcModule.add(number_1, number_2)
   print(f"Result: {result}")
elif operat == "subtract":
    result = calcModule.subtract(number_1, number_2)
    print(f"Result: {result}")
elif operat == "multiply":
    result = calcModule.multiply(number_1, number_2)
    print(f"Result: {result}")
elif operat == "divide":
    result = calcModule.divide(number_1, number_2)
    print(f"Result: {result}")
else:
    print("ERROR INVALID REQUEST")