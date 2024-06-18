class Calculator:
    def addition(self, num1, num2):
        return num1+num2
        
    def subtraction(self, num1, num2):
            return num1-num2 
    def multiplication(self, num1, num2):
            return num1*num2
    def division(self, num1, num2):
            if num2==0:
                return "cannot be divide by Zero!"
            else:
                return num1 / num2
            

calculator = Calculator()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


if operation == '+':
    result = calculator.addition(num1, num2)
    print("Result:", result)
elif operation == '-':
    result = calculator.subtraction(num1, num2)
    print("Result:", result)
elif operation == '*':
    result = calculator.multiplication(num1, num2)
    print("Result:", result)
elif operation == '/':
    result = calculator.division(num1, num2)
    print("Result:", result)
else:
    print("Invalid operation!")