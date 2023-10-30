#tell whether a user input an uppercase, lowercase, or number 0-9

#input

char = input("Input any charachter:")

#calc and output

if char >= 'A' and char <= 'Z':
    print("Uppercase character was entered")
elif char >= 'a' and char <= 'z':
    print("Lowercase character was entered")
elif '9' >= char >= '0':
    print("A number was entered")
