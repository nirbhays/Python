#Calculator
def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    is_true=True
    num1=float(input("What's the first number?: "))
    while is_true:
        for keys in operations:
            print(keys)
        operations_symbol=input("Pick an operation from above line symbol: ")
        num2=float(input("What's the next number?: "))
        #op=operations[operations_symbol]
        answer=(float (operations[operations_symbol](num1, num2)))
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        go_again=str(input(f"Type 'y' to continue operation with {answer} or 'n' to exit: "))
        num1=answer
        if go_again!="y":
            is_true=False
            calculator()
calculator()
    