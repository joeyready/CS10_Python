#Joseph Ready
#1300529
#Homework 1 Program Set 1
#This program will compute the monthly payment and total payment of a loan.

#Data/input
annual_int_rate = float(input("Enter annual interest rate, (e.g., 7.25) : "))
length_in_years = int(input("Enter number years as an interger, (e.g., 5) : "))   
loan_amt = float(input("Enter loan amount, (e.g., 120000.95) : "))

#calc
length_in_months = (length_in_years * 12)
monthly_int_rate = (annual_int_rate / 1200)
monthly_payment = loan_amt * monthly_int_rate / (1-1/(1 + monthly_int_rate) ** (length_in_years *12))
total_paid = (monthly_payment * length_in_months)

#output
print ('\nThe monthly payment is' , (format(monthly_payment , ',.2f')))
print ('The total payment is' , (format(total_paid , ',.2f')))


##Test Run 1
##Enter annual interest rate, (e.g., 7.25) : 4.5
##Enter number years as an interger, (e.g., 5) : 30
##Enter loan amount, (e.g., 120000.95) : 350000.50
##
##
##The monthly payment is 1,773.40
##The total payment is 638,424.40
##
##Test Run 2
##Enter annual interest rate, (e.g., 7.25) : 2.45
##Enter number years as an interger, (e.g., 5) : 4
##Enter loan amount, (e.g., 120000.95) : 13529.75
##
##
##The monthly payment is 296.19
##The total payment is 14,217.33
##
##Test Run 3
##Enter annual interest rate, (e.g., 7.25) : 1
##Enter number years as an interger, (e.g., 5) : 1
##Enter loan amount, (e.g., 120000.95) : 1
##
##
##The monthly payment is 0.08
##The total payment is 1.01
##
##Test Run 4
##Enter annual interest rate, (e.g., 7.25) : 69
##Enter number years as an interger, (e.g., 5) : 69
##Enter loan amount, (e.g., 120000.95) : 420
##
##
##The monthly payment is 24.15
##The total payment is 19,996.20
##
##Test Run 5
##Enter annual interest rate, (e.g., 7.25) : 3.68
##Enter number years as an interger, (e.g., 5) : 5
##Enter loan amount, (e.g., 120000.95) : 21325.68
##
##
##The monthly payment is 389.67
##The total payment is 23,380.37    
