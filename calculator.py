def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def exponent(x, y):
    return x ** y

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

print("Welcome to Simple Calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")

choice = input("Enter choice from above peration (1/2/3/4/5): ")

if choice in ('1', '2', '3', '4', '5'):
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", exponent(num1, num2))
else:
    print("Invalid input")
