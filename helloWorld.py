#input to get user age
userAge = int(input("Please input your age: "))
#input to get user's name
userName = str(input("Please enter your name: "))
#input to get user's postcode
userPostCode = str(input("Please enter your home postcode: "))

#print out the user's inputs
print(userName)
print(userAge)
print(userPostCode)

#function to add two numbers
def addNums(x, y):
    #the addition and output
    addingTogether = x + y
    print(f"The answer to {x} + {y} is: {addingTogether}")

#calling the function and getting two numbers from the user
addNums(int(input("Please enter the first number for the addition: ")), int(input("Please enter the second number for the addition: ")))