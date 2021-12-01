from art import logo

# add


def add(n1, n2):
    return n1+n2

# substract


def substract(n1, n2):
    return n1 - n2

# multiply


def multiply(n1, n2):
    return n1 * n2

# divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What is the first number? : "))
    for symbols in operations:
        print(symbols)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation for the line above : ")
        num2 = float(input("What is the second number? : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. : ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
