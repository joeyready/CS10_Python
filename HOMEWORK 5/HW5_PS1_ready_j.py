# Joseph Ready
# 1300529
# Homework 5 Program Set 1
# This program calculates and displays the loan's monthly payment and total payment amount for the user.

# Initiate Clas 'Loan'
class Loan:
    def __init__(self, annual_rate: float = 2.5, length_in_years: int = 1, loan_amt: float = 1000, borrowers_name: str = ""):
        self.__annual_rate = annual_rate
        self.__length_in_years = length_in_years
        self.__loan_amt = loan_amt
        self.__borrowers_name = borrowers_name

    def get_annual_rate(self) -> float:
        """This method gets user input for interest rate of their loan"""
        return self.__annual_rate

    def get_length_in_years(self) -> int:
        """This method takes user input for length of loan"""
        return self.__length_in_years

    def get_loan_amt(self) -> float:
        """This method get users loan amount"""
        return self.__loan_amt

    def get_borrowers_name(self) -> str:
        """This method gets user's name"""
        return self.__borrowers_name

    def set_annual_rate(self, new_rate):
        """This method sets the annual rate of the loan"""
        self.__annual_rate = new_rate

    def set_length_in_years(self, new_length):
        """This method sets the length of the loan"""
        self.__length_in_years = new_length

    def set_loan_amt(self, new_amt):
        """This Method Sets Loan Amount"""
        self.__loan_amt = new_amt

    def set_borrowers_name(self, new_name):
        """This method sets the borrowers name"""
        self.__borrowers_name = new_name

    def getMonthlyPayment(self):
        """Calculates Monthly Payment"""
        monthly_interest_rate = self.__annual_rate / 1200
        return self.__loan_amt * monthly_interest_rate / (1 - (1/(1 + monthly_interest_rate) ** (self.__length_in_years * 12)))

    def getTotalPayment(self):
        """Calculates Total Payments of Loan"""
        return self.getMonthlyPayment() * self.__length_in_years * 12\


def main():

    rate = float(input("Enter yearly interest rate: "))
    length = int(input("Enter number of years as an integer: "))
    amt = float(input("Enter loan amount: "))
    name = input("Enter a borrower's name: ")
    loan1 = Loan(rate, length, amt, name)
    print("The loan is for", loan1.get_borrowers_name())
    print("The monthly payment is", format(loan1.getMonthlyPayment(), '.2f'))
    print("The total payment is", format(loan1.getTotalPayment(), '.2f'))

    user_input = input("\nDo you want to change the loan amount? Y for yes or enter to quit ")
    while user_input == 'Y' or user_input == 'y':
        amt = float(input("Enter new loan amount: "))
        loan1.set_loan_amt(amt)
        print("The loan is for", loan1.get_borrowers_name())
        print("The monthly payment is", format(loan1.getMonthlyPayment(), '.2f'))
        print("The total payment is", format(loan1.getTotalPayment(), '.2f'))
        user_input = input("\nDo you want to change the loan amount? Y for yes or enter to quit ")
    else:
        print("")

if __name__ == "__main__":
    main()


# Test Run 1
#
# Enter yearly interest rate: 2.5
# Enter number of years as an integer: 5
# Enter loan amount: 1000.00
# Enter a borrower's name: John Jones
# The loan is for John Jones
# The monthly payment is 17.75
# The total payment is 1064.84
#
# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount: 5000
# The loan is for John Jones
# The monthly payment is 88.74
# The total payment is 5324.21
#
# Do you want to change the loan amount? Y for yes or enter to quit
#
#
# Test Run 2
# Enter yearly interest rate: 7.5
# Enter number of years as an integer: 6
# Enter loan amount: 23500.00
# Enter a borrower's name: Joey Ready
# The loan is for Joey Ready
# The monthly payment is 406.32
# The total payment is 29254.87
#
# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount: 20000
# The loan is for Joey Ready
# The monthly payment is 345.80
# The total payment is 24897.76
#
# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount: 17000
# The loan is for Joey Ready
# The monthly payment is 293.93
# The total payment is 21163.10
#
# Do you want to change the loan amount? Y for yes or enter to quit
#
#
# Test Run 4
#
# Enter yearly interest rate: 5.25
# Enter number of years as an integer: 12
# Enter loan amount: 357843
# Enter a borrower's name: Elon Musk
# The loan is for Elon Musk
# The monthly payment is 3354.71
# The total payment is 483078.54
#
# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount: 5000000
# The loan is for Elon Musk
# The monthly payment is 46874.08
# The total payment is 6749867.15
#
# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount: 650000000000
# The loan is for Elon Musk
# The monthly payment is 6093630064.70
# The total payment is 877482729317.24
#
# Do you want to change the loan amount? Y for yes or enter to quit
#
#
# Test Run 5
#
# Enter yearly interest rate: 25.25
# Enter number of years as an integer: 20
# Enter loan amount: 1000
# Enter a borrower's name:  Jack Smith
# The loan is for  Jack Smith
# The monthly payment is 21.18
# The total payment is 5084.34
#
# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount: 100
# The loan is for  Jack Smith
# The monthly payment is 2.12
# The total payment is 508.43
#
# Do you want to change the loan amount? Y for yes or enter to quit y
# Enter new loan amount: 250
# The loan is for  Jack Smith
# The monthly payment is 5.30
# The total payment is 1271.09
#
# Do you want to change the loan amount? Y for yes or enter to quit
