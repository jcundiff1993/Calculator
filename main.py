from art import logo

def add (n1, n2):
    """Adds two numbers together."""
    return n1 + n2
def subtract (n1, n2):
    """Subtracts one number from another."""
    return n1 - n2
def multiply (n1, n2):
    """Multiplies two numbers together."""
    return n1 * n2
def divide (n1, n2):
    """Divides one number by another."""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def do_math():
    '''Starts the calculator function without pre-existing numbers'''
    print(logo)
    end_calculation = False
    print("Welcome to Pycharmer calculator.\n")

    num1 = float(input("Enter the first number:\n"))
    while not end_calculation:

        print("Choose your operand:")
        for symbols in operations:
            print(symbols)
        print("_______________")
        operand = input("")

        calculation_function = operations[operand]

        num2 = float(input("Enter the next number:\n"))


        answer = calculation_function(num1, num2)

        print(f"{num1} {operand} {num2} = {answer}")
        num1 = answer
        more_math = input(f"Continue calculation with {answer}? 'Yes' or 'No \n")
        more_math = more_math.title()
        if more_math == "No":
            do_math()
do_math()




