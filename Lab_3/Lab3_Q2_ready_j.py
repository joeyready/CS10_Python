def show_interest(rate : float = 0.01 , period : int = 10 , principal : float = 10000.00) -> None:
    """calculates interest and prints it"""
    interest = principal * rate * period
    print("The simple interest will be $" , format(interest , ",.2f"), sep = '')


def main():
    show_interest()


if __name__ == "__main__":
    main()


# Test Run 1
# The simple interest will be $1,000.00
#
# Test Run 2
# The simple interest will be $1,000.00
#
# Test Run 1
# The simple interest will be $1,000.00
