# Joseph Ready
# 1300529
# Homework 5 Program Set 1
# This program calculates and displays the loan for a car.

class Loan:
    def __init__(self, annual_rate: float = 2.5, length_in_years: int = 1, loan_amt: float = 1000, borrowers_name: str = ""):
        self.__annual_rate = annual_rate
        self.__length_in_years = length_in_years
        self.__loan_amt = loan_amt
        self.__borrowers_name = borrowers_name

    def get_annual_rate(self) -> float:
        return self.__annual_rate

    def get_length_in_years(self) -> int:
        return self.__length_in_years

    def get_loan_amt(self) -> float:
        return self.__loan_amt

    def get_borrowers_name(self) -> str:
        return self.__borrowers_name

    def set_annual_rate(self, new_rate):
        self.__annual_rate = new_rate

    def set_length_in_years(self, new_length):
        self.__length_in_years = new_length

    def set_loan_amt(self, new_amt):
        self.__loan_amt = new_amt

    def set_borrowers_name(self, new_name):
        self.__borrowers_name = new_name

    def getMonthlyPayment(self):
        monthly_interest_rate = self.__annual_rate / 1200
        return self.__loan_amt * monthly_interest_rate / (1 - (1/(1 + monthly_interest_rate) ** (self.__length_in_years * 12)))

    def getTotalPayment(self):
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

if __name__ == "__main__":
    main()