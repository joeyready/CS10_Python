#Lab 7 Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order. 

#input
userinput = 4321
#calc
num1 = userinput // 1000
num1remainder = userinput % 1000
num2 = num1remainder // 100
num2remainder = num1remainder % 100
num3 = num2remainder // 10
num3remainder = num2remainder % 10

#output
print(num3remainder,num3,num2,num1,sep='')
