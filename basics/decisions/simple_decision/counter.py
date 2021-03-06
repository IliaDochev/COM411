print("Please enter the first whole number:")
number1 = int(input()) #Requesting the first number from the user and storing it in variable "number1"

print("Please enter the second whole number:")
number2 = int(input()) #Requesting the second number from the user and storing it in variable "number2"

print("Please enter the third whole number:")
number3 = int(input()) # Requesting the third number from the user and storing it in variable "number3"

even = 0 #Declaring our two counter variables that the program is going to use to store the amount of even and odd numbers.
odd = 0

if(number1 % 2 == 0): #In this line we check if the first number is odd or even using the modulo operator.

  even = even + 1 #If the above statement comes back as true. This line increments the counter variable "even" by 1.
else: #If the check is false, the program comes back to this default statement which increments the "odd" counter variable by one.
  odd = odd + 1

if(number2 % 2 == 0): #Same as line 13
  even = even + 1
else: # Same as line 16
  odd = odd + 1

if(number3 % 2 == 0): #Same as line 13
  even = even + 1
else: #Same as line 16
  odd = odd + 1

print("There are {} even and {} odd numbers.".format(even,odd)) #After all the checks have been performed, the program prints to the console the amount of odd and even numbers.

