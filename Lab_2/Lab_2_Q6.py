#calculate property tax

#input
lot = int(input("Enter the lot number or enter -999 to end : "))
prop_value = float(input("Enter property value : "))

#calc
tax = prop_value * .0065

#output

while lot != -999:
    print ("$" + format(tax , ".2f"))

    lot = int(input("\nEnter the lot number or enter -999 to end : "))
    prop_value = float(input("Enter property value : "))
