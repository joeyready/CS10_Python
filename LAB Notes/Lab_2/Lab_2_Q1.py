#Lab 2 Q1

#input
age = int(input("Enter the age:"))

#calc and output
if age >= 18:
    print("You are eligible to cast your vote")
else:
    print("You have to wait for another" , 18 - age , "years to cast your vote")
