# Calculator
from CalArt import logo

# Add
def add(n1,n2):
  return n1 + n2

# Subtract
def subtract(n1,n2):
  return n1 - n2

# Multiply
def multiply(n1,n2):
  return n1 * n2

# Divide
def divide(n1,n2):
  return n1 / n2

operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operators:
    print(symbol)
  should_continue = True

  while should_continue:
    first_operator_symbol = input("Pick an operator from the line above: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operators[first_operator_symbol]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {first_operator_symbol} {num2} = {first_answer}")

    if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = first_answer
    else:
      should_continue = False
calculator()
