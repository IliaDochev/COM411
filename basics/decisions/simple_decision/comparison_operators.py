print("Please enter the first number:") #Requesting the first number from the user
number1 = int(input()) #Storing the first number in variable "number1"

print("Please enter the second number:") #Requesting the second number from the user
number2 = int(input()) #Storing the second number in variable "number2"

if(number1>number2): #Comapring the two numbers to check if the first number is bigger than the second one. If it is, the below statement will be printet to the user.
  print("The second number is the smallest")

else: #If the above check is false, the program prints the below statement to the user.
  print("The first number is the smallest")