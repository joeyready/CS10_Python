# Joseph Ready
# 1300529
# Homework 2 Program Set 1
# This program calculates profit/loss on a stock trade.

def load() -> (str , int , float , float , float):
    """collects user input for name, # of shares, purchase price, sale price, and commission rate"""
    print()
    name = input("Enter Stock name: ")
    shares = int(input("Enter Number of Shares : "))
    pur_price = float(input("Enter Purchase price : "))
    sale_price = float(input("Enter selling price : "))
    comm_rate = float(input("Enter Commission : "))
    return name , shares , pur_price , sale_price , comm_rate


def calc(shares , pur , sale , comm) -> (float , float , float , float , float):
    """Calculates data base on user input"""
    amt_paid = shares * pur
    comm_paid = amt_paid * comm
    amt_sold = shares * sale
    sale_comm = amt_sold * comm
    profit = (amt_sold - sale_comm)-(amt_paid + comm_paid)
    return amt_paid , comm_paid , amt_sold , sale_comm , profit


def output(name: str , amt_paid: float , comm_paid: float , amt_sold: float , sale_comm: float , profit: float):
    """Prints the amount paid, commission paid, and amount sold, profit and commission"""
    print()
    print()
    print("Stock name : " , name)
    print("Amount paid for the stock:          $" , format(amt_paid , "13,.2f"))
    print("Commission paid on the purchase:    $" , format(comm_paid , "13,.2f"))
    print("Amount the stock sold for:          $" , format(amt_sold , "13,.2f"))
    print("Commission paid on the sale:        $" , format(sale_comm , "13,.2f"))
    print("Profit (or loss if negative):       $" , format(profit , "13,.2f"))
    print()
    print()


def main():
    user_input = input("Enter your stock information? Type 'y' for yes, or 'n' for no: ")

    while user_input == "y":
        name , shares , pur_price , sale_price , comm_rate = load()
        amt_paid , comm_paid , amt_sold , sale_comm , profit = calc(shares , pur_price , sale_price , comm_rate)
        output(name , amt_paid , comm_paid , amt_sold , sale_comm , profit)

        user_input = input("Enter your stock information? Type 'y' for yes, or 'n' for no: ")


if __name__ == "__main__":
    main()


##Test Run 1
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Kaplack, Inc.
##Enter Number of Shares : 10000
##Enter Purchase price : 33.92
##Enter selling price : 35.92
##Enter Commission : 0.04
##
##
##Stock name :  Kaplack, Inc.
##Amount paid for the stock:          $    339,200.00
##Commission paid on the purchase:    $     13,568.00
##Amount the stock sold for:          $    359,200.00
##Commission paid on the sale:        $     14,368.00
##Profit (or loss if negative):       $     -7,936.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: IBM
##Enter Number of Shares : 15000
##Enter Purchase price : 50.25
##Enter selling price : 100.20
##Enter Commission : 0.02
##
##
##Stock name :  IBM
##Amount paid for the stock:          $    753,750.00
##Commission paid on the purchase:    $     15,075.00
##Amount the stock sold for:          $  1,503,000.00
##Commission paid on the sale:        $     30,060.00
##Profit (or loss if negative):       $    704,115.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##Test Run 2
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##Test Run 3
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Apple
##Enter Number of Shares : 1000
##Enter Purchase price : 43.25
##Enter selling price : 24.37
##Enter Commission : 0.05
##
##
##Stock name :  Apple
##Amount paid for the stock:          $     43,250.00
##Commission paid on the purchase:    $      2,162.50
##Amount the stock sold for:          $     24,370.00
##Commission paid on the sale:        $      1,218.50
##Profit (or loss if negative):       $    -22,261.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Tesla
##Enter Number of Shares : 40000
##Enter Purchase price : 190.21
##Enter selling price : 74.88
##Enter Commission : .025
##
##
##Stock name :  Tesla
##Amount paid for the stock:          $  7,608,400.00
##Commission paid on the purchase:    $    190,210.00
##Amount the stock sold for:          $  2,995,200.00
##Commission paid on the sale:        $     74,880.00
##Profit (or loss if negative):       $ -4,878,290.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##
##Test Run 4
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Ford Motor Co.
##Enter Number of Shares : 1750
##Enter Purchase price : 23.45
##Enter selling price : 135.78
##Enter Commission : 0.02
##
##
##Stock name :  Ford Motor Co.
##Amount paid for the stock:          $     41,037.50
##Commission paid on the purchase:    $        820.75
##Amount the stock sold for:          $    237,615.00
##Commission paid on the sale:        $      4,752.30
##Profit (or loss if negative):       $    191,004.45
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Coca Cola
##Enter Number of Shares : 1500
##Enter Purchase price : 75.75
##Enter selling price : 75.98
##Enter Commission : 0.03
##
##
##Stock name :  Coca Cola
##Amount paid for the stock:          $    113,625.00
##Commission paid on the purchase:    $      3,408.75
##Amount the stock sold for:          $    113,970.00
##Commission paid on the sale:        $      3,419.10
##Profit (or loss if negative):       $     -6,482.85
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Sony
##Enter Number of Shares : 25000
##Enter Purchase price : 125.84
##Enter selling price : 137.82
##Enter Commission : 0.05
##
##
##Stock name :  Sony
##Amount paid for the stock:          $  3,146,000.00
##Commission paid on the purchase:    $    157,300.00
##Amount the stock sold for:          $  3,445,500.00
##Commission paid on the sale:        $    172,275.00
##Profit (or loss if negative):       $    -30,075.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
##Test Run 5
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Canon
##Enter Number of Shares : 1004
##Enter Purchase price : 75.56
##Enter selling price : 87.32
##Enter Commission : .02
##
##
##Stock name :  Canon
##Amount paid for the stock:          $     75,862.24
##Commission paid on the purchase:    $      1,517.24
##Amount the stock sold for:          $     87,669.28
##Commission paid on the sale:        $      1,753.39
##Profit (or loss if negative):       $      8,536.41
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Nikon
##Enter Number of Shares : 1435
##Enter Purchase price : 24.24
##Enter selling price : 34.34
##Enter Commission : .023
##
##
##Stock name :  Nikon
##Amount paid for the stock:          $     34,784.40
##Commission paid on the purchase:    $        800.04
##Amount the stock sold for:          $     49,277.90
##Commission paid on the sale:        $      1,133.39
##Profit (or loss if negative):       $     12,560.07
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n


