#input
sugar = 1.5/48
butter = 1/48
flour = 2.75/48

#userinput
cookiesneeded = int(input("How many cookies do you want to bake?"))

#calc
sugarneeded = sugar*cookiesneeded
butterneeded = butter*cookiesneeded
flourneeded = flour*cookiesneeded

#output
print('To make', cookiesneeded, 'cookies, you will need:')
print(format(sugarneeded, '.2f'),'cups of sugar')
print(format(butterneeded, '.2f'), 'cups of butter')
print(format(flourneeded, '.2f'),'cups of flour')
