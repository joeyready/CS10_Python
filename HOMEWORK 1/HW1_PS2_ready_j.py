#Joseph Ready
#1300529
#Homework 1 Program Set 2
#This program will calculate the profit or loss a stock sale (including commissions).

#input
stock_name = input("Enter Stock Name : ")
num_of_shares = int(input("Enter Number of shares : "))
purchase_price = float(input("Enter Purchase Price : "))
selling_price = float(input("Enter selling price : "))
broker_commission = float(input("Enter Commission : "))
                    
#calc
amt_paid = num_of_shares * purchase_price
pur_commission_paid = amt_paid * broker_commission
amt_sold = num_of_shares * selling_price
sale_commission_paid = amt_sold * broker_commission
profit = (amt_sold - sale_commission_paid)-(amt_paid + pur_commission_paid)

#output
print()
print()
print("Amount paid for the stock:          $" , (format(amt_paid , "13,.2f")))
print("Commission paid on the purchase:    $" , (format(pur_commission_paid , "13,.2f")))
print("Amount the stock sold for:          $" , (format(amt_sold , "13,.2f")))
print("Commission paid on the sale:        $" , (format(sale_commission_paid , "13,.2f")))
print("Profit (or loss if negative):       $" , (format(profit , "13,.2f")))



##Test Run 1
##Enter Stock Name : Kaplack, Inc.
##Enter Number of shares : 10000
##Enter Purchase Price : 33.92
##Enter selling price : 35.92
##Enter Commission : 0.04
##
##
##Amount paid for the stock:          $    339,200.00
##Commission paid on the purchase:    $     13,568.00
##Amount the stock sold for:          $    359,200.00
##Commission paid on the sale:        $     14,368.00
##Profit (or loss if negative):       $     -7,936.00

##Test Run 2
##Enter Stock Name : IBM
##Enter Number of shares : 15000
##Enter Purchase Price : 50.25
##Enter selling price : 100.20
##Enter Commission : 0.02
##
##
##Amount paid for the stock:          $    753,750.00
##Commission paid on the purchase:    $     15,075.00
##Amount the stock sold for:          $  1,503,000.00
##Commission paid on the sale:        $     30,060.00
##Profit (or loss if negative):       $    704,115.00

##Test Run 3
##Enter Stock Name : Enron
##Enter Number of shares : 25000
##Enter Purchase Price : 350.74
##Enter selling price : 0.03
##Enter Commission : .07
##
##
##Amount paid for the stock:          $  8,768,500.00
##Commission paid on the purchase:    $    613,795.00
##Amount the stock sold for:          $        750.00
##Commission paid on the sale:        $         52.50
##Profit (or loss if negative):       $ -9,381,597.50

##Test Run 4
##Enter Stock Name : Tesla
##Enter Number of shares : 20000
##Enter Purchase Price : 12.12
##Enter selling price : 782.93
##Enter Commission : .025
##
##
##Amount paid for the stock:          $    242,400.00
##Commission paid on the purchase:    $      6,060.00
##Amount the stock sold for:          $ 15,658,600.00
##Commission paid on the sale:        $    391,465.00
##Profit (or loss if negative):       $ 15,018,675.00

##Test Run 5
##Enter Stock Name : Coca Cola
##Enter Number of shares : 105
##Enter Purchase Price : 75.25
##Enter selling price : 75.97
##Enter Commission : .03
##
##
##Amount paid for the stock:          $      7,901.25
##Commission paid on the purchase:    $        237.04
##Amount the stock sold for:          $      7,976.85
##Commission paid on the sale:        $        239.31
##Profit (or loss if negative):       $       -400.74
