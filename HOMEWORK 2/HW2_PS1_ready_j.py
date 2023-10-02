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
    print(rand_num)
    if user_num == rand_num:
        print("Exact match: You win $10,000!")

    elif user_dig_1 == rand_num_dig_2 and user_dig_2 == rand_num_dig_1:
        print("Match all digits : You win $3,000")

    elif user_dig_1 == rand_num_dig_1 or user_dig_1 == rand_num_dig_2 or user_dig_2 == rand_num_dig_1 or user_dig_2 == rand_num_dig_2:
        print("Match one digit: You win $1,000")

    else:
        print("Sorry no match")

    user_num = int(input("Enter your lottery pick ( 2 digits) or -999 to quit: "))
