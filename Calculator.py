# Calculator

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

num1 = int(input("What's the first number?: "))

for symbol in operators:
  print(symbol)
first_operator_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operators[first_operator_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {first_operator_symbol} {num2} = {first_answer}")

second_operator_symbol = input("Pick another operator: ")
num3 = int(input("What's the third number?: "))

calculation_function = operators[second_operator_symbol]

second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {second_operator_symbol} {num3} = {second_answer}")