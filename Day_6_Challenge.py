# If we have an application that'asks a user for their phone number
# Give it the phone number 1254 or 090.
# For example, when you enter 1234, the program should translate it to words
# One Two Three Four
# and prints out "One Two Three Four" without the quotes

print("Welcome to number to word converter")
phone_number = input("Enter your phone number in digits: ")
num_mapping = {
    "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",
}
# print(num_mapping["0"])
output = ""
if phone_number.isdigit():
    for num in phone_number:
        output = output + num_mapping[num] + " "
    print(output)
else:
    print("Please enter a number digit")