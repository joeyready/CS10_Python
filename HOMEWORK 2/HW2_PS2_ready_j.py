#Joseph Ready
#1300529
#Homework 2 Program Set 2
#This program will calculate federal income tax based on user input.

#Data/input
income = int(input("Enter income as an integer with no commas: "))

while income >= 0:
    
#calc
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

#calculate 2018 tax

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
    print(income)
    print("2017 tax: " , (format(tax_2017 , '.2f')))
    print("2018 tax: " , (format(tax_2018 , '.2f')))
    print("Difference:" , (format(tax_diff_amt , '.2f')))
    print("Difference (percent):" , (format(tax_diff_pct * 100 , '.2f')))

    income = int(input("Enter income as an integer with no commas: "))
