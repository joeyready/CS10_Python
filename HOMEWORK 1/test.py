# Data/input
annual_int_rate = int(input("Enter your annual interest rate:"))
length_in_years = int(input("Enter number of years for the loan:"))
loan_amt = int(input("What is the total amount of the loan?"))

length_in_months = length_in_years * 12

# Calculate
monthly_int_rate = annual_int_rate / 1200
monthly_payment = loan_amt * monthly_int_rate / (1 - 1 / (1 + monthly_int_rate) ** length_in_months)
total_paid = monthly_payment * length_in_months

# Output with right-aligned dollar signs
print(f'The monthly payment is: ${monthly_payment:,.2f}')
print(f'The total payment is: ${total_paid:,.2f}')
print(length_in_months)
