# Alcohol limit and associated punishment

# Write a drunk driving application that decides if a driver is above alcohol limit and give an appropriate punishment


# Input the name of the driver and then the alcohol level and the program should print out below information:
# Alcohol level in mg
# The fine
# The punishment
# Use below requirement for your program:
# 0 = OK and no alcohol in the blood
# greater than 0 but less or equal to 0.2 mg = OK, but driver has (alcohol level) in the blood
# greater than 0.2 mg but less than 0.5 mg = 20,000 SEK fine and Ban for 1 year
# Above 0.5 mg = 6 months prison, Ban for 3 year, Fine based on 10% of your yearly salary


name_driver = input("What is the name of driver: ")
try:
    alcohol_level = float(input("What is his/her alcohol level in mg: "))
    if alcohol_level == 0:
        print("Driver is Okay and no alcohol in the blood")
    elif alcohol_level > 0 and alcohol_level <= 0.2:
        print("Driver is Okay and has alcohol in the blood")
    elif alcohol_level > 0.2 and alcohol_level <= 0.5:
        print("Driver is banned for 1 year and fined 20,000 SEK")
    elif alcohol_level > 0.5:
        print("Driver is imprisoned for 6 months, banned for 3 years and fined 10% of his/her yearly salary")

except NameError:
    print("The input is invalid, please check and try again")
except ValueError:
    print("Please try again")


