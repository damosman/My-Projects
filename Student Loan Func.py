# Write a  python program
# Define a  student loan function
# Only students that have an income are eligible for a loan
# All students without an income will get the message "Sorry, you are not eligible for a loan"

# If a student earns below 15,000 they cannot get a loan at 30% yearly interest and a duration of 5 years
# Print out the monthly payment in this case for teh student

# Students earning 15,000 and above can get a loan with a yearly interest of 10% and a duration of 7 years
# Print out the monthly payment in this case for the student

# You need to input the loan amount, duration and the interest to calculate the monthly payment and print it out.


# slf is student loan function
def student_loan(s):
    # s is student income
    if s <= 0:
        print("Sorry, You are not eligible for a loan")
    elif s > 0 and s < 15000:
        print("You cannot get a loan at 30% yearly interest and a duration of 5 years")
    elif s > 15000:
        print("Congrats!, You can get a loan at 10% yearly interest and a duration of 7 years")

student_loan(int(input("Enter Your yearly income: " + "SEK ")))
def slf(p,i,n):
    # p = loan amount
    # 0.01 is origination fee
    p = p + (p * 0.01)
    # i = effective interest rate
    i = (i/100)/12
    # n = duration of repayment
    n = n * 12
    # m = monthly repayments
    m = p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    print(round(m))

slf(p = int(input("Enter Amount the amount needed for Your student loan: ")), n = int(input("Enter the number of years for repayment: ")), i = int(input("Enter the interest rate: ")))


