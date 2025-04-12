
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print("Result is :", result)
    print("Result is :", result1)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Please enter a numerical value.")

except NameError as ex:
    print("The exception is ", ex)
finally:
    print("I will always excute no matter what.")