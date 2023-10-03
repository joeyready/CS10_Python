#Joseph Ready
#1300529
#Homework 2 Program Set 2
#This program will calculate 2017 and 2018 income tax based on user input.

#Data/input
income = int(input("Enter income as an integer with no commas: "))

while income >= 0:
    
#calc 2017 tax
    if income <= 9325:
        tax_2017 = income * .1
    elif income <= 37950:
        tax_2017 = (income - 9325) * .15 + (9325 * .1)
    elif income <= 91900:
        tax_2017 = (income - 37950) * .25 + ((37950 - 9325) * .15) + (9325 * .1)
    elif income <= 191650:
        tax_2017 = (income - 91900) * .28 + ((91900 - 37950) * .25) + ((37950 - 9325) * .15) + (9325 * .1)
    elif income <= 416700:
        tax_2017 = (income - 191650) * .33 + ((191650 - 91900) * .28) + ((91900 - 37950) * .25) + ((37950 - 9325) * .15) + (9325 * .1)
    elif income <= 418400:
        tax_2017 = (income - 416700) * .35 + ((416700 - 191650) * .33) + ((191650 - 91900) * .28) + ((91900 - 37950) * .25) + ((37950 - 9325) * .15) + (9325 * .1)
    elif income > 418400:
        tax_2017 = (income - 418400) * .396 + ((418400 - 416700) * .35) + ((416700 - 191650) * .33) + ((191650 - 91900) * .28) + ((91900 - 37950) * .25) + ((37950 - 9325) * .15) + (9325 * .1)

#2018 tax

    if income <= 9525:
        tax_2018 = income * .1
    elif income <= 38700:
        tax_2018 = (income - 9525) * .12 + (9525 * .1)
    elif income <= 82500:
        tax_2018 = (income - 38700) * .22 + ((38700 - 9525) * .12) + (9525 * .1)
    elif income <= 157500:
        tax_2018 = (income - 82500) * .24 + ((82500 - 38700) * .22) + ((38700 - 9525) * .12) + (9525 * .1)
    elif income <= 200000:
        tax_2018 = (income - 157500) * .32 + ((157500 - 82500) * .24) + ((82500 - 38700) * .22) + ((38700 - 9525) * .12) + (9525 * .1)
    elif income <= 500000:
        tax_2018 = (income - 200000) * .35 + ((200000 - 157500) * .32) + ((157500 - 82500) * .24) + ((82500 - 38700) * .22) + ((38700 - 9525) * .12) + (9525 * .1)
    elif income > 500000:
        tax_2018 = (income - 500000) * .37 + ((500000 - 200000) * .35) + ((200000 - 157500) * .32) + ((157500 - 82500) * .24) + ((82500 - 38700) * .22) + ((38700 - 9525) * .12) + (9525 * .1)

#tax_2018 = 987349

    
    #total_tax
    #2017_tax
    #2018_tax
    tax_diff_amt = tax_2018 - tax_2017
    tax_diff_pct = abs(tax_diff_amt / tax_2017)


    #output
    print("Income: " , (income))
    print("2017 tax: " , (format(tax_2017 , '.2f')))
    print("2018 tax: " , (format(tax_2018 , '.2f')))
    print("Difference:" , (format(tax_diff_amt , '.2f')))
    print("Difference (percent):" , (format(tax_diff_pct * 100 , '.2f')))

    income = int(input("\nEnter income as an integer with no commas: "))


##Test Run 1
##Income:  8000
##2017 tax:  800.00
##2018 tax:  800.00
##Difference: 0.00
##Difference (percent): 0.00
##    
##Enter income as an integer with no commas: 15000
##Income:  15000
##2017 tax:  1783.75
##2018 tax:  1609.50
##Difference: -174.25
##Difference (percent): 9.77
##    
##Enter income as an integer with no commas: 40000
##Income:  40000
##2017 tax:  5738.75
##2018 tax:  4739.50
##Difference: -999.25
##Difference (percent): 17.41
##    
##Enter income as an integer with no commas: 100000
##Income:  100000
##2017 tax:  20981.75
##2018 tax:  18289.50
##Difference: -2692.25
##Difference (percent): 12.83
##    
##Enter income as an integer with no commas: 200000
##Income:  200000
##2017 tax:  49399.25
##2018 tax:  45689.50
##Difference: -3709.75
##Difference (percent): 7.51
##    
##Enter income as an integer with no commas: 500000
##Income:  500000
##2017 tax:  153818.85
##2018 tax:  150689.50
##Difference: -3129.35
##Difference (percent): 2.03
##    
##Enter income as an integer with no commas: 1000000
##Income:  1000000
##2017 tax:  351818.85
##2018 tax:  335689.50
##Difference: -16129.35
##Difference (percent): 4.58
##    
##Enter income as an integer with no commas: 10000000
##Income:  10000000
##2017 tax:  3915818.85
##2018 tax:  3665689.50
##Difference: -250129.35
##Difference (percent): 6.39
##    
##Enter income as an integer with no commas: -1
##
##Test Run 2
##
##Enter income as an integer with no commas: -1
##
##Test Run 3
##
##Enter income as an integer with no commas: 22222
##Income:  22222
##2017 tax:  2867.05
##2018 tax:  2476.14
##Difference: -390.91
##Difference (percent): 13.63
##
##Enter income as an integer with no commas: 333333
##Income:  333333
##2017 tax:  93399.14
##2018 tax:  92356.05
##Difference: -1043.09
##Difference (percent): 1.12
##
##Enter income as an integer with no commas: 4444444
##Income:  4444444
##2017 tax:  1715818.67
##2018 tax:  1610133.78
##Difference: -105684.89
##Difference (percent): 6.16
##
##Enter income as an integer with no commas: 55555
##Income:  55555
##2017 tax:  9627.50
##2018 tax:  8161.60
##Difference: -1465.90
##Difference (percent): 15.23
##
##Enter income as an integer with no commas: -1
##
##Test Run 4
##
##Enter income as an integer with no commas: 12345
##Income:  12345
##2017 tax:  1385.50
##2018 tax:  1290.90
##Difference: -94.60
##Difference (percent): 6.83
##
##Enter income as an integer with no commas: 54321
##Income:  54321
##2017 tax:  9319.00
##2018 tax:  7890.12
##Difference: -1428.88
##Difference (percent): 15.33
##
##Enter income as an integer with no commas: 2468
##Income:  2468
##2017 tax:  246.80
##2018 tax:  246.80
##Difference: 0.00
##Difference (percent): 0.00
##
##Enter income as an integer with no commas: 135790
##Income:  135790
##2017 tax:  31002.95
##2018 tax:  26879.10
##Difference: -4123.85
##Difference (percent): 13.30
##
##Enter income as an integer with no commas: -1
##
##Test Run 5
##
##Enter income as an integer with no commas: 55222
##Income:  55222
##2017 tax:  9544.25
##2018 tax:  8088.34
##Difference: -1455.91
##Difference (percent): 15.25
##
##Enter income as an integer with no commas: 662345
##Income:  662345
##2017 tax:  218107.47
##2018 tax:  210757.15
##Difference: -7350.32
##Difference (percent): 3.37
##
##Enter income as an integer with no commas: 762345
##Income:  762345
##2017 tax:  257707.47
##2018 tax:  247757.15
##Difference: -9950.32
##Difference (percent): 3.86
##
##Enter income as an integer with no commas: 91827365
##Income:  91827365
##2017 tax:  36319455.39
##2018 tax:  33941814.55
##Difference: -2377640.84
##Difference (percent): 6.55
##
##Enter income as an integer with no commas: -1
