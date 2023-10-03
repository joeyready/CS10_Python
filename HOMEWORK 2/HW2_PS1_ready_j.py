#Joseph Ready
#1300529
#Homework 2 Program Set 1
#This program will be a lottery game where a user will enter a 2 digit number and try to match a randomly generated 2 digit number.

import random

#Data/input

user_num = int(input("Enter your lottery pick ( 2 digits) or -999 to quit: "))

while user_num != -999:
    rand_num = random.randint(1,100)  

#calc
    user_dig_1 = user_num//10
    user_dig_2 = user_num%10
    rand_num_dig_1 = rand_num//10
    rand_num_dig_2 = rand_num%10


#output
#print(rand_num)
    if user_num == rand_num:
        print("Exact match: You win $10,000!")

    elif user_dig_1 == rand_num_dig_2 and user_dig_2 == rand_num_dig_1:
        print("Match all digits : You win $3,000")

    elif user_dig_1 == rand_num_dig_1 or user_dig_1 == rand_num_dig_2 or user_dig_2 == rand_num_dig_1 or user_dig_2 == rand_num_dig_2:
        print("Match one digit: You win $1,000")

    else:
        print("Sorry no match")

    user_num = int(input("\nEnter your lottery pick ( 2 digits) or -999 to quit: "))

##Test Run 1
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 44
##Exact match: You win $10,000!
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 23
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 68
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 12
##Match one digit: You win $1,000
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 45
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##
##Test Run 2
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 34
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 56
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 67
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 78
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 89
##Match one digit: You win $1,000
##
##Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##
##Test Run 3
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 98
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 87
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 76
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 65
##Match one digit: You win $1,000
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 54
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##Test Run 4
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 13
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 24
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 35
##Match one digit: You win $1,000
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 46
##Match one digit: You win $1,000
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 57
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: -999
##
##Test Run 5
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 91
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 82
##Match one digit: You win $1,000
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 73
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 64
##Match one digit: You win $1,000
##
##Enter your lottery pick ( 2 digits) or -999 to quit: 55
##Sorry no match
##
##Enter your lottery pick ( 2 digits) or -999 to quit: -999
