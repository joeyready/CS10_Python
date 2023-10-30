def string_total(num_string):
    """Adds each digit from the string together"""
    total = 0
    for digit in num_string:
        total += int(digit)
    return total


def main():
    #Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits with nothing separating them:')

    # Call string_total function, and store the total.
    total = string_total(number_string)

    # Display the total.
    print('The total of the digits in the string you entered is', total)


#calls main
if __name__ == "__main__":
    main()

#Test Run 1
##Enter a sequence of digits with nothing separating them:4563
##The total of the digits in the string you entered is 18

#Test Run 2
##Enter a sequence of digits with nothing separating them:653214
##The total of the digits in the string you entered is 21

#Test Run 3
##Enter a sequence of digits with nothing separating them:1234576
##The total of the digits in the string you entered is 28
