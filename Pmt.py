# Write a Python mortgage function called - pmt
# That calculates your monthly payment based on the principal, interest and number of payments

# Amount = Principal
# Interest
# Duration = n = number of payments
# Monthly Payment

# M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]



def pmt(p,i,n):
    # p = Loan payment
    i = (i/100)/12
    # n = duration of repayment
    n = n * 12
    # i = interest rate
    m = p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    print(round(m))

pmt(p = int(input("Enter Amount the amount needed for Your mortgage: ")), n = int(input("Enter the number of years for repayment: ")), i = int(input("Enter the interest rate: ")))


