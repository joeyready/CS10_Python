# This program calculates a salesperson's pay
def get_sales() -> float:
    """User inputs their sales amt"""
    sales = float(input("Enter the monthly sales: "))
    return sales


def get_advanced_pay() -> float:
    """gets advanced pay"""
    print("Enter the amount of advanced pay, or")
    print("enter 0 if no advanced pay was given.")
    advanced_pay = float(input("Advanced pay: "))
    return advanced_pay


def determine_comm_rate(sales : float):
    """calculates user's commission rate"""
    if sales < 10000:
        rate = .10
    elif sales < 15000:
        rate = .12
    elif sales < 18000:
        rate = .14
    elif sales < 22000:
        rate = .16
    else:
        rate = .18
    return rate
    

def main():

    # Get the amount of sales from user
    sales = get_sales()

    # Get the amount of advanced pay from user.
    advanced_pay = get_advanced_pay()

    # Determine the commission rate.
    comm_rate = determine_comm_rate(sales)

    # Calculate the pay.
    pay = sales * comm_rate - advanced_pay

    # Display the amount of pay.
    print('The pay is $', format(pay, ',.2f'), sep='')

    # Determine whether the pay is negative.
    if pay < 0:
        print('The salesperson must reimburse')
        print('the company.')


if __name__ == "__main__":
    main()

#Test Run 1
##Enter the monthly sales: 14550.00
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 1000.00
##The pay is $746.00

#Test Run 2
##Enter the monthly sales: 9500
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 0
##The pay is $950.00

#Test Run 3
##Enter the monthly sales: 12000.00
##Enter the amount of advanced pay, or
##enter 0 if no advanced pay was given.
##Advanced pay: 2000.00
##The pay is $-560.00
##The salesperson must reimburse
##the company.
