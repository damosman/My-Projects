# Write a Python program that takes as input a pre-formatted string of phrases/sentences mixed with numbers like below:
# What is the main reason for leaving?
# 21
# Happy Easter Holidays
# 40
# All the men here are just not understanding the situation
# Happy Easter Holidays
# 50
# In what ways can I help you
# Happy Easter Holidays
# You better learn how to be polite
# 100
# Happy Easter Holidays
# OMG that food is looking really great
# Happy Easter Holidays
# 100
# 800
# 900
# Well, let us try to think about that in another way
# Notice that 5 lines of the string have the phrase “Happy Easter Holidays” repeated, while there are additional six sentences that are not repeated, as well as numbers inserted on a few lines.
# Your task is to:
# •	Print out the strings like below:
# •	Extract the 5 repeated phrase and print to the terminal
# •	Extract the non-repeated phrase and print to the terminal
# •	Extract all the numbers and print to the terminal
# Note: Make sure you write a pseudocode to capture your thought process before writing any line of code. The pseudocode is also part of the assignment. If any question(s), ask your co-students and if still unresolved, you can ask me.


string1 = ("21")
string2 = ("Happy Easter Holidays")
string3 = ("40")
string4 = ("All the men here are just not understanding the situation")
string5 = ("Happy Easter Holidays")
string6 = ("50")
string7 = ("In what ways can I help you")
string8 = ("Happy Easter Holidays")
string9 = ("You better learn how to be polite")
string10 = ("100")
string11 = ("Happy Easter Holidays")
string12 = ("OMG that food is looking really great")
string13 = ("Happy Easter Holidays")
string14 = ("100")
string15 = ("800")
string16 = ("900")
string17 = ("Well, let us try to think about that in another way")

# print(len(string1))

# the 5 repeated phrase

slice1 = slice(0, 21)
slice2 = slice(0, 21)
slice3 = slice(0, 21)
slice4 = slice(0, 21)
slice5 = slice(0, 21,)

# print statement for 5 repeated phrase
print(string2[slice1])
print(string5[slice2])
print(string8[slice3])
print(string11[slice4])
print(string13[slice5])

# the non-repeated phrase and print to the terminal
slice6 = slice(0, 57)
slice7 = slice(0, 27)
slice8 = slice(0, 33)
slice9 = slice(0, 37)
slice10 = slice(0, 51)

# print statement for the non-repeated phrase and print to the terminal
print(string4[slice6])
print(string7[slice7])
print(string9[slice8])
print(string12[slice9])
print(string17[slice10])

# all the numbers
slice11 = slice(2)
slice12 = slice(2)
slice13 = slice(3)
slice14 = slice(3)
slice15 = slice(3)
slice16 = slice(3)
slice17 = slice(3)

# print all the numbers
print(string1[slice6])
print(string3[slice7])
print(string6[slice8])
print(string10[slice9])
print(string14[slice10])
print(string15[slice10])
print(string16[slice10])

