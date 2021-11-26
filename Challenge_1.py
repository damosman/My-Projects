# Challenge_1
welcome_message = "Hello, Welcome to TecVinson AB"
print(welcome_message)
firstName = input("First Name: ")
lastName = input("Last Name: ")
address = input("Address: ")
weight_in_kg = input("Weight in kg: ")
weight_in_kg_integer = float(weight_in_kg)
pounds_kg_converter = 0.45
weight_in_pounds = weight_in_kg_integer * pounds_kg_converter
# print(type(weight_in_pounds))

weight_in_pounds_int = int(weight_in_pounds)
# print(type(weight_in_pounds_int))

age = input("Age: ")
nationality = input("Nationality: ")
sex = input("Gender: ")
message = f"{firstName} {lastName} lives at {address}. He weighs {weight_in_kg} kg and {weight_in_pounds} pounds. He is a {nationality}."
print(message)

# git hurray

