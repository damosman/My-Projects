# Write a function in Python that calculates the addition, subtraction, division and multiplication of any 4 numbers that you enter

# The __future__ method is to avoid the ZeroDivisionError in case the user enters zero as input
from __future__ import division
# The function will print out the following


# Addition = the result of addition (i.e. an integer number)
a = (input("Enter first digit number: "))
b = (input("Enter second digit number: "))
c = (input("Enter third digit number: "))
d = (input("Enter fourth digit number: "))

if a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit():
    def add_numbers():
        addition = int(a) + int(b) + int(c) + int(d)
        return addition
    print(add_numbers())
else:
    print("Please enter a number")


# Subtraction = the result of subtraction (i.e. an integer number - beware of not having a negative number)
e = (input("\n" "Enter first digit number: "))
f = (input("Enter second digit number: "))
g = (input("Enter third digit number: "))
h = (input("Enter fourth digit number: "))

if e.isdigit() and f.isdigit() and g.isdigit() and h.isdigit():
    def sub_numbers():
        subtraction = (int(e) - int(f) - int(g) - int(h) * -1)
        return subtraction
    print(sub_numbers())
else:
    print("Please enter a number")


# Multiplication = the result of multiplication (i.e. an integer number)

i = (input("\n" "Enter first digit number: "))
j = (input("Enter second digit number: "))
k = (input("Enter third digit number: "))
l = (input("Enter fourth digit number: "))

if i.isdigit() and j.isdigit() and k.isdigit() and l.isdigit():
    def mul_numbers():
        multiplication = int(i) * int(j) * int(k) * int(l)
        return multiplication
    print(mul_numbers())
else:
    print("Please enter a number")


# Division = the result of division (i.e. a float number)

m = (input("\n" "Enter first digit number: "))
n = (input("Enter second digit number: "))
o = (input("Enter third digit number: "))
p = (input("Enter fourth digit number: "))

if m.isdigit() and n.isdigit() and o.isdigit() and p.isdigit():
    def div_numbers():
        division = float(m) / float(n) / float(o) / float(p)
        return division
    print(round(div_numbers(), 2))
else:
    print("Please enter a number")


