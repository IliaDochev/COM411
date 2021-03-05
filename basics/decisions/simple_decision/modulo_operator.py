print("Please enter a whole number:") #Request a number from the user
number = int(input()) #Store the user's choice in the "number" variable


if (number % 2 == 0): #Using the modulo operator to devide the users choice by 2 and if the remainder is 0, the program prints the below result. If not, the program goes to the default statement.
  print("\n\n{} is an even number".format(number))

else: #If the above statement is false the program runs this bit of code informing the user that his number is an odd one.
  print("\n\n{} is a odd number".format(number))