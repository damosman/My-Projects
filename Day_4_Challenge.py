# Write a python program that does below:
#-----------------------------
# Ask the user to input a temperature in °F
# Convert the temperature entered from to °C
# if temperature is greater than 30
    # print "it's a hot day"
# otherwise if it's less than 10
    # print "it's a cold day"
# otherwise
    # print "it's neither hot nor cold"
#-----------------------------


print("Hello, Welcome to Daily Weather Prediction")
try:
    tempFahrenheit = input("Enter the air temperature in °F: ")
    tempCelsius = (float(tempFahrenheit) -32)/ 1.8
    print(f"You have entered",round(tempCelsius,2),"°C")

    if tempCelsius > 30:
        print("It's a hot day")
    elif tempCelsius < 10:
        print("It's a cold day")
    else:
        print("It's neither hot nor cold")
except NameError:
    print("The input is invalid, please check and try again")
except ValueError:
    print("Please try again")
